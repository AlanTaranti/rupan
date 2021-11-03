from typing import List

import boto3
from botocore.exceptions import ProfileNotFound


class BaseRepository:
    def __init__(self, profile="default"):
        self.profile = profile

    @property
    def session(self):
        try:
            return boto3.Session(profile_name=self.profile)
        except ProfileNotFound:
            exit("Perfil {}, não encontrado!".format(self.profile))
