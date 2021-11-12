from datetime import datetime, timedelta

import pandas as pd
from botocore.exceptions import ClientError

from .repository.sts_repository import StsRepository
from .repository.iam_repository import IamRepository


class AccessKeyService:
    def __format_get_access_keys(self, dataframe: pd.DataFrame):
        dataframe = dataframe.rename(
            columns={
                "UserName": "username",
                "AccessKeyId": "access_key",
                "Status": "status",
                "CreateDate": "create_date",
                "LastUsedDate": "last_used_date",
                "ServiceName": "last_used_service_name",
                "Region": "last_used_region",
            }
        )
        dataframe["never_used"] = dataframe["last_used_date"].isnull()

        one_year_ago = datetime.utcnow().date() - timedelta(days=365)
        dataframe["last_use_greater_than_one_year"] = (
            pd.to_datetime(dataframe["last_used_date"]).dt.date < one_year_ago
        )

        return dataframe

    def get_access_keys(self):
        repository = IamRepository()
        sts_repository = StsRepository()

        try:
            access_keys = repository.list_access_keys()
        except ClientError as error:
            exit(error)

        if len(access_keys) == 0:
            return pd.DataFrame(
                columns=[
                    "account_id",
                    "username",
                    "access_key",
                    "status",
                    "create_date",
                    "last_used_date",
                    "last_used_service_name",
                    "last_used_region",
                    "never_used",
                    "last_use_greater_than_one_year",
                ]
            )

        access_keys = pd.DataFrame(access_keys)

        account_id = sts_repository.get_account_id()
        access_keys.insert(0, "account_id", account_id)

        access_keys = self.__format_get_access_keys(access_keys)

        return access_keys
