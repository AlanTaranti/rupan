from datetime import datetime, timedelta

import pandas as pd
from botocore.exceptions import ClientError

from .repository.sts_repository import StsRepository
from .repository.s3_repository import S3Repository
from .repository.cloudfront_repository import CloudfrontRepository


class LoggingService:
    def __format_get_logging(self, dataframe: pd.DataFrame):
        dataframe = dataframe.rename(
            columns={
                "Name": "name",
                "LoggingEnabled": "logging_enabled",
            }
        )

        return dataframe

    def get_logging(self):
        s3_repository = S3Repository()
        sts_repository = StsRepository()
        cloudfront_repository = CloudfrontRepository()

        try:
            buckets_logging = s3_repository.list_buckets_logging()
        except ClientError as error:
            exit(error)

        try:
            cloudfront_logging = cloudfront_repository.list_distributions_logging()
        except ClientError as error:
            exit(error)

        buckets_logging = pd.DataFrame(buckets_logging)
        buckets_logging.insert(0, "service", "s3")

        cloudfront_logging = pd.DataFrame(cloudfront_logging)
        cloudfront_logging.insert(0, "service", "cloudfront")

        dataframe = pd.concat([buckets_logging, cloudfront_logging])
        account_id = sts_repository.get_account_id()
        dataframe.insert(0, "account_id", account_id)

        dataframe = self.__format_get_logging(dataframe)

        return dataframe
