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
            }
        )
        return dataframe

    def get_access_keys(self, format="pandas"):
        repository = IamRepository()
        sts_repository = StsRepository()

        try:
            access_keys = repository.list_access_keys()
        except ClientError as error:
            exit(error)

        if format == "list":
            return access_keys

        try:
            access_keys = repository.list_access_keys()
        except ClientError as error:
            exit(error)

        access_keys = pd.DataFrame(access_keys)
        account_id = sts_repository.get_account_id()
        access_keys.insert(0, "account_id", account_id)
        access_keys = self.__format_get_access_keys(access_keys)

        return access_keys
