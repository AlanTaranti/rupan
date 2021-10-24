from dataclasses import dataclass
from typing import List, Optional

from .tag import Tag


@dataclass
class IpRange:

    Status: str
    CidrIp: str
    Description: str
    Tags: Optional[List[Tag]]
