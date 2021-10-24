import fire
import pandas as pd

from src.security_group_service import SecurityGroupService


def AwsSgExtractor():
    """
    Um simples extrator de Security Groups da AWS
    """

    # Obter os security groups
    service = SecurityGroupService()
    security_groups = service.get_security_groups()

    # tratar os security groups
    for security_group in security_groups:
        name = security_group["GroupName"]
        filename = "{}.xlsx".format(name)

        ## Metadados
        metadata = {
            "group_name": security_group["GroupName"],
            "owner_id": security_group["OwnerId"],
            "group_id": security_group["GroupId"],
            "vpc_id": security_group["VpcId"],
            "description": security_group["Description"],
        }
        metadata = pd.DataFrame([metadata])

        ## Ip Permissions
        ip_permissions = pd.DataFrame(security_group["IpPermissions"])

        ## Ip Permissions Egress
        ip_permissions_egress = pd.DataFrame(security_group["IpPermissionsEgress"])

        with pd.ExcelWriter(filename, mode="w") as writer:
            metadata.to_excel(writer, "metadata", index=False)
            ip_permissions.to_excel(writer, "ip_permissions_inbound", index=False)
            ip_permissions_egress.to_excel(
                writer, "ip_permissions_outbound", index=False
            )


if __name__ == "__main__":
    fire.Fire(AwsSgExtractor)
