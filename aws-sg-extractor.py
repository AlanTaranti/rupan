import os
from collections import OrderedDict

import fire
import pandas as pd

from src.security_group_service import SecurityGroupService


def ip_permissions_formatter(ip_permissions: pd.DataFrame, prefix) -> pd.DataFrame:
    ip_permissions = ip_permissions.rename(
        columns={
            "FromPort": "{}_from_port".format(prefix),
            "IpProtocol": "{}_ip_protocol".format(prefix),
            "IpRanges": "{}_ipv4_ranges".format(prefix),
            "Ipv6Ranges": "{}_ipv6_ranges".format(prefix),
            "PrefixListIds": "{}_prefix_list_ids".format(prefix),
            "ToPort": "{}_to_port".format(prefix),
            "UserIdGroupPairs": "{}_user_id_group_pairs".format(prefix),
        }
    )

    columns = [
        "{}_ip_protocol".format(prefix),
        "{}_to_port".format(prefix),
        "{}_to_port".format(prefix),
        "{}_ipv4_ranges".format(prefix),
        "{}_ipv6_ranges".format(prefix),
        "{}_prefix_list_ids".format(prefix),
        "{}_user_id_group_pairs".format(prefix),
    ]

    ip_permissions = ip_permissions.reindex(columns=columns)

    return ip_permissions


def aws_sg_extractor(profile: str = "default"):
    """
    Um simples extrator de Security Groups da AWS
    """

    # Obter os security groups
    service = SecurityGroupService(profile=profile)
    security_groups = service.get_security_groups()

    # Criar diretorio de saida de arquivos
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, "{}.csv".format(profile))

    dataframes = []
    # tratar os security groups
    for security_group in security_groups:

        # Metadados
        metadata = OrderedDict(
            {
                "group_name": security_group["GroupName"],
                "owner_id": security_group["OwnerId"],
                "group_id": security_group["GroupId"],
                "vpc_id": security_group["VpcId"],
                "description": security_group["Description"],
            }
        )
        metadata = OrderedDict(reversed(list(metadata.items())))

        # Ip Permissions
        ip_permissions_inbound = pd.DataFrame(security_group["IpPermissions"])
        ip_permissions_inbound = ip_permissions_formatter(
            ip_permissions_inbound, "ip_permissions_inbound"
        )

        # Ip Permissions Egress
        ip_permissions_outbound = pd.DataFrame(security_group["IpPermissionsEgress"])
        ip_permissions_outbound = ip_permissions_formatter(
            ip_permissions_outbound, "ip_permissions_outbound"
        )

        dataframe = pd.concat([ip_permissions_inbound, ip_permissions_outbound], axis=1)

        for key, value in metadata.items():
            dataframe.insert(0, key, value)

        dataframes.append(dataframe)

    dataframes = pd.concat(dataframes)
    dataframes.to_csv(filepath, index=False)


if __name__ == "__main__":
    fire.Fire(aws_sg_extractor)
