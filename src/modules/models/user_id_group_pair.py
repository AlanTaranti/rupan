from dataclasses import dataclass


@dataclass
class UserIdGroupPair:

    Description: str
    GroupId: str
    GroupName: str
    PeeringStatus: str
    UserId: str
    VpcId: str
    VpcPeeringConnectionId: str
