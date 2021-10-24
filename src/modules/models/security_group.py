from dataclasses import dataclass
from typing import List

from .ip_permission import IpPermission
from .tag import Tag


@dataclass
class SecurityGroup:

    Description: str
    GroupName: str
    IpPermissions: List[IpPermission]
    OwnerId: str
    GroupId: str
    IpPermissionsEgress: List[IpPermission]
    Tags: List[Tag]
    VpcId: str
