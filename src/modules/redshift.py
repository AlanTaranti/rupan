from typing import List
import boto3
from botocore.exceptions import ClientError

from .models.cluster_security_group import ClusterSecurityGroup
from .base import BaseModule


class Redshift(BaseModule):
    @property
    def client(self):
        return boto3.client("redshift")

    def get_segurity_groups(self) -> List[ClusterSecurityGroup]:
        try:
            return self.client.describe_cluster_security_groups()[
                "ClusterSecurityGroups"
            ]
        except ClientError:
            # Clientes VPC-by-Default não podem usar Grupos de Segurança no Redshift
            return []
