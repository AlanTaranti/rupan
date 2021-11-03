from typing import List

from .base import BaseRepository


class Ec2(BaseRepository):
    @property
    def client(self):
        return self.session.client("ec2")

    def get_segurity_groups(self) -> List:
        return self.client.describe_security_groups()["SecurityGroups"]
