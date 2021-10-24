from dataclasses import dataclass
from typing import List, Optional

from .tag import Tag


@dataclass
class EC2SecurityGroup:

    Status: Optional[str]
    EC2SecurityGroupName: str
    EC2SecurityGroupId: str
    EC2SecurityGroupOwnerId: str
    Tags: Optional[List[Tag]]
