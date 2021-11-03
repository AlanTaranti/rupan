from typing import List

import boto3
from botocore.exceptions import ProfileNotFound


class BaseRepository:
    def __init__(self, profile="default", region_name: str = None):
        self.profile = profile
        self.region_name = region_name

    @property
    def session(self):
        try:
            return boto3.Session(
                profile_name=self.profile, region_name=self.region_name
            )
        except ProfileNotFound:
            exit("Perfil {}, não encontrado!".format(self.profile))
