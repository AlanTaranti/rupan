from typing import List

import boto3
from botocore.exceptions import ProfileNotFound


class BaseRepository:
    def __init__(self, region_name: str = None):
        self.region_name = region_name

    @property
    def session(self):
        return boto3.Session(region_name=self.region_name)
