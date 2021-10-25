from typing import List

from .modules.ec2 import Ec2


class SecurityGroupService:
    def __init__(self, profile):
        self.profile = profile

    def get_security_groups(self) -> List:
        return Ec2(self.profile).get_segurity_groups()
