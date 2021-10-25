import fire
import pandas as pd

from src.security_group_service import SecurityGroupService


def ip_permissions_formatter(ip_permissions: pd.DataFrame) -> pd.DataFrame:
    ip_permissions = ip_permissions.rename(
        columns={
            "FromPort": "from_port",
            "IpProtocol": "ip_protocol",
            "IpRanges": "ipv4_ranges",
            "Ipv6Ranges": "ipv6_ranges",
            "PrefixListIds": "prefix_list_ids",
            "ToPort": "to_port",
            "UserIdGroupPairs": "user_id_group_pairs",
        }
    )

    columns = [
        "ip_protocol",
        "from_port",
        "to_port",
        "ipv4_ranges",
        "ipv6_ranges",
        "prefix_list_ids",
        "user_id_group_pairs",
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

    # tratar os security groups
    for security_group in security_groups:
        name = security_group["GroupName"]
        filename = "{}.xlsx".format(name)

        # Metadados
        metadata = {
            "group_name": security_group["GroupName"],
            "owner_id": security_group["OwnerId"],
            "group_id": security_group["GroupId"],
            "vpc_id": security_group["VpcId"],
            "description": security_group["Description"],
        }
        metadata = pd.DataFrame([metadata])

        # Ip Permissions
        ip_permissions_inbound = pd.DataFrame(security_group["IpPermissions"])
        ip_permissions_inbound = ip_permissions_formatter(ip_permissions_inbound)

        # Ip Permissions Egress
        ip_permissions_outbound = pd.DataFrame(security_group["IpPermissionsEgress"])
        ip_permissions_outbound = ip_permissions_formatter(ip_permissions_outbound)

        with pd.ExcelWriter(filename, mode="w") as writer:
            metadata.to_excel(writer, "metadata", index=False)
            ip_permissions_inbound.to_excel(
                writer, "ip_permissions_inbound", index=False
            )
            ip_permissions_outbound.to_excel(
                writer, "ip_permissions_outbound", index=False
            )


if __name__ == "__main__":
    fire.Fire(aws_sg_extractor)
