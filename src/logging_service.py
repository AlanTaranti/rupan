from datetime import datetime, timedelta

import pandas as pd
from botocore.exceptions import ClientError

from .repository.sts_repository import StsRepository
from .repository.s3_repository import S3Repository


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
        repository = S3Repository()
        sts_repository = StsRepository()

        try:
            buckets_logging = repository.list_buckets_logging()
        except ClientError as error:
            exit(error)

        buckets_logging = pd.DataFrame(buckets_logging)
        buckets_logging.insert(0, "service", "s3")

        dataframe = pd.concat([buckets_logging])
        account_id = sts_repository.get_account_id()
        dataframe.insert(0, "account_id", account_id)

        dataframe = self.__format_get_logging(dataframe)

        return dataframe
