from dataclasses import dataclass
from typing import List

from src.modules.models.ip_range import IpRange
from src.modules.models.tag import Tag

from .ec2_security_group import EC2SecurityGroup


@dataclass
class CacheSecurityGroup:

    OwnerId: str
    CacheSecurityGroupName: str
    Description: str
    EC2SecurityGroups: List[EC2SecurityGroup]
    ARN: str
