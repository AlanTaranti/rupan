from typing import List

from botocore.exceptions import ClientError

from .modules.ec2 import Ec2


class SecurityGroupService:
    def __init__(self, profile):
        self.profile = profile

    def get_security_groups(self) -> List:
        try:
            return Ec2(self.profile).get_segurity_groups()
        except ClientError as error:
            exit(error)
