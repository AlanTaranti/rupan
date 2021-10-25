from typing import List

import boto3


class BaseModule:
    def __init__(self, profile="default"):
        self.profile = profile

    @property
    def session(self):
        return boto3.Session(profile_name=self.profile)

    def get_segurity_groups(self) -> List:
        raise NotImplementedError()
