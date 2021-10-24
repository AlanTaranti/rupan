from dataclasses import dataclass
from typing import List

from src.modules.models.ip_range import IpRange

from .ec2_security_group import EC2SecurityGroup


@dataclass
class DbSecurityGroup:

    OwnerId: str
    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    VpcId: str
    EC2SecurityGroups: List[EC2SecurityGroup]
    IPRanges: List[IpRange]
    DBSecurityGroupArn: str
