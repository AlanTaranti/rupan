from typing import List
import boto3

from .models.db_security_group import DbSecurityGroup
from .base import BaseModule


class Rds(BaseModule):
    @property
    def client(self):
        return boto3.client("rds")

    def get_segurity_groups(self) -> List[DbSecurityGroup]:
        return self.client.describe_db_security_groups()["DBSecurityGroups"]
