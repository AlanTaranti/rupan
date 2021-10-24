from dataclasses import dataclass


@dataclass
class IpRange:

    Status: str
    CidrIp: str
    Description: str
