from datetime import datetime, timedelta

from src.logger import logger
from src.repository.cloudwatch_repository import CloudwatchRepository
from src.repository.lambda_repository import LambdaRepository


class LambdaService:
    def __init__(self):
        self.lambda_repository = LambdaRepository()
        self.cloudwatch_repository = CloudwatchRepository()

    def list_inactive_lambdas(self, days: int) -> list:
        # Calculate the threshold date based on the provided number of days
        threshold_date = datetime.now() - timedelta(days=days)

        paginator = self.lambda_repository.get_paginator()
        response_iterator = paginator.paginate()

        inactive_functions = []

        for page in response_iterator:
            for function in page['Functions']:
                logger.debug("Getting last invocation time for function: %s", function['FunctionName'])
                function_name = function['FunctionName']
                last_invocation_time = self._get_last_invocation_time(function_name)
                logger.debug("Last invocation time for function %s: %s", function_name, last_invocation_time)

                if not last_invocation_time or last_invocation_time < threshold_date:
                    logger.debug("Function %s is inactive", function_name)
                    inactive_functions.append(function_name)

        return inactive_functions

    def _get_last_invocation_time(self, function_name: str):
        """
        Retrieve the last invocation time of a Lambda function from its CloudWatch log group.
        """
        log_group_name = f"/aws/lambda/{function_name}"
        streams = self.cloudwatch_repository.describe_log_streams(log_group_name)
        if streams is not None and 'logStreams' in streams and streams['logStreams']:
            last_event_timestamp = streams['logStreams'][0]['lastEventTimestamp']
            return datetime.fromtimestamp(last_event_timestamp / 1000)
        return None
