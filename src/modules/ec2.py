from typing import List
import boto3

from .models.security_group import SecurityGroup
from .base import BaseModule


class Ec2(BaseModule):
    @property
    def client(self):
        return boto3.client("ec2")

    def get_segurity_groups(self) -> List[SecurityGroup]:
        return self.client.describe_security_groups()["SecurityGroups"]
