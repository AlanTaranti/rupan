import pandas as pd
from botocore.exceptions import ClientError

from .repository.iam_repository import IamRepository


class AccessKeyService:
    def __format_get_access_keys(self, dataframe: pd.DataFrame):
        return dataframe

    def get_access_keys(self, format="pandas"):
        repository = IamRepository()

        try:
            access_keys = repository.list_access_keys()
        except ClientError as error:
            exit(error)

        if format == "list":
            return access_keys

        access_keys = pd.DataFrame(access_keys)
        access_keys = self.__format_get_access_keys(access_keys)

        return access_keys
