from typing import List
from collections import OrderedDict

from botocore.exceptions import ClientError
import pandas as pd

from .repository.ec2_repository import Ec2Repository


def ip_permissions_formatter(ip_permissions: pd.DataFrame, prefix) -> pd.DataFrame:
    columns_dict = {
        "from_port": "{}_from_port".format(prefix),
        "ip_protocol": "{}_ip_protocol".format(prefix),
        "ipv4_ranges": "{}_ipv4_ranges".format(prefix),
        "ipv6_ranges": "{}_ipv6_ranges".format(prefix),
        "prefix_list_ids": "{}_prefix_list_ids".format(prefix),
        "to_port": "{}_to_port".format(prefix),
        "user_id_group_pairs": "{}_user_id_group_pairs".format(prefix),
    }

    ip_permissions = ip_permissions.rename(
        columns={
            "FromPort": columns_dict["from_port"],
            "IpProtocol": columns_dict["ip_protocol"],
            "IpRanges": columns_dict["ipv4_ranges"],
            "Ipv6Ranges": columns_dict["ipv6_ranges"],
            "PrefixListIds": columns_dict["prefix_list_ids"],
            "ToPort": columns_dict["to_port"],
            "UserIdGroupPairs": columns_dict["user_id_group_pairs"],
        }
    )

    columns = [
        columns_dict["ip_protocol"],
        columns_dict["from_port"],
        columns_dict["to_port"],
        columns_dict["ipv4_ranges"],
        columns_dict["ipv6_ranges"],
        columns_dict["prefix_list_ids"],
        columns_dict["user_id_group_pairs"],
    ]

    ip_permissions = ip_permissions.reindex(columns=columns)

    ip_permissions[columns_dict["from_port"]] = ip_permissions[
        columns_dict["from_port"]
    ].astype("Int64")
    ip_permissions[columns_dict["to_port"]] = ip_permissions[
        columns_dict["to_port"]
    ].astype("Int64")

    return ip_permissions


class SecurityGroupService:
    def get_security_groups(self, region_name: str = None) -> List:
        try:
            return Ec2Repository(region_name).get_segurity_groups()
        except ClientError as error:
            exit(error)

    def get_regions(self) -> List:
        try:
            return Ec2Repository().get_regions()
        except ClientError as error:
            exit(error)

    def to_pandas(self) -> pd.DataFrame:
        regions = self.get_regions()

        dataframes = []
        for region in regions:
            region_dataframe = self.to_pandas_region(region)
            if region_dataframe is not None:
                dataframes.append(region_dataframe)

        dataframes = pd.concat(dataframes)
        return dataframes

    def to_pandas_region(self, region_name: str = None) -> pd.DataFrame:
        security_groups = self.get_security_groups(region_name)

        if len(security_groups) == 0:
            return None

        dataframes = []
        # tratar os security groups
        for security_group in security_groups:

            # Metadados
            metadata = OrderedDict(
                {
                    "account_id": security_group.get("OwnerId"),
                    "group_name": security_group.get("GroupName"),
                    "group_id": security_group.get("GroupId"),
                    "vpc_id": security_group.get("VpcId"),
                    "description": security_group.get("Description"),
                }
            )
            metadata = OrderedDict(reversed(list(metadata.items())))

            # Ip Permissions
            ip_permissions_inbound = pd.DataFrame(security_group["IpPermissions"])
            ip_permissions_inbound = ip_permissions_formatter(
                ip_permissions_inbound, "ip_permissions_inbound"
            )

            # Ip Permissions Egress
            ip_permissions_outbound = pd.DataFrame(
                security_group["IpPermissionsEgress"]
            )
            ip_permissions_outbound = ip_permissions_formatter(
                ip_permissions_outbound, "ip_permissions_outbound"
            )

            dataframe = pd.concat(
                [ip_permissions_inbound, ip_permissions_outbound], axis=1
            )

            for key, value in metadata.items():
                dataframe.insert(0, key, value)

            dataframes.append(dataframe)

        dataframes = pd.concat(dataframes)
        dataframes.insert(1, "region_name", region_name)

        return dataframes
