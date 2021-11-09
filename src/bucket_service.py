from datetime import datetime, timedelta

import pandas as pd
from botocore.exceptions import ClientError

from .repository.sts_repository import StsRepository
from .repository.s3_repository import S3Repository


class BucketService:
    def __format_get_buckets(self, dataframe: pd.DataFrame):
        dataframe = dataframe.rename(
            columns={
                "Name": "name",
                "DisplayName": "owner",
                "LocationConstraint": "region",
                "IsPublic": "is_public",
            }
        )

        return dataframe

    def get_buckets(self):
        repository = S3Repository()
        sts_repository = StsRepository()

        try:
            buckets = repository.list_buckets_data()
        except ClientError as error:
            exit(error)

        buckets = pd.DataFrame(buckets)

        account_id = sts_repository.get_account_id()
        buckets.insert(0, "account_id", account_id)

        buckets = self.__format_get_buckets(buckets)

        return buckets
