from typing import List
import boto3


from .models.cache_security_group import CacheSecurityGroup
from .base import BaseModule


class Elasticache(BaseModule):
    @property
    def client(self):
        return boto3.client("elasticache")

    def get_segurity_groups(self) -> List[CacheSecurityGroup]:
        try:
            return self.client.describe_cache_security_groups()["CacheSecurityGroups"]
        except:
            # Dependendo da versão da conta na AWS, o uso de SG no Elastic Cache não é permitido
            return []
