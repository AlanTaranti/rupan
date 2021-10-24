from dataclasses import dataclass


@dataclass
class EC2SecurityGroup:

    Status: str
    EC2SecurityGroupName: str
    EC2SecurityGroupId: str
    EC2SecurityGroupOwnerId: str
