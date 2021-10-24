from typing import List

from .modules.ec2 import Ec2


class SecurityGroupService:
    def get_security_groups(self) -> List:
        return Ec2().get_segurity_groups()
