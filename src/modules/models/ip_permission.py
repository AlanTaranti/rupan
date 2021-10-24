from dataclasses import dataclass
from typing import List

from .ip_range import IpRange
from .ipv6_range import Ipv6Range
from .prefix_list_id import PrefixListId
from .user_id_group_pair import UserIdGroupPair


@dataclass
class IpPermission:

    FromPort: int
    IpProtocol: str
    IpRanges: List[IpRange]
    IpRanges: List[Ipv6Range]
    PrefixListIds: List[PrefixListId]
    ToPort: int
    UserIdGroupPairs: List[UserIdGroupPair]
