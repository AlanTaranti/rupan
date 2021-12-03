from typing import List

from .base_repository import BaseRepository
from ..logger import logger


class Ec2Repository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("ec2")

    @property
    def resource(self):
        return self.session.resource("ec2")

    def get_all_ec2_instances(self):
        return self.resource.instances.all()

    def get_all_ec2_security_groups_ids(self):
        logger.debug("Getting EC2 Instances from {}".format(self.region_name))
        instances = self.get_all_ec2_instances()

        security_groups_ids = []
        for instance in instances:
            security_groups = instance.security_groups
            if security_groups is not None:
                for security_group in security_groups:
                    security_groups_ids.append(security_group["GroupId"])

        return list(set(security_groups_ids))

    def get_vpc(self, id: str):
        logger.debug("Getting VPC {}".format(id))
        return self.resource.Vpc(id)

    def get_segurity_groups(self) -> List:
        logger.debug("Getting Security Groups from {}".format(self.region_name))
        used_security_groups_ids = self.get_all_ec2_security_groups_ids()
        security_groups_consolidated = self.client.describe_security_groups()[
            "SecurityGroups"
        ]

        # Has Resources
        security_groups = []
        for security_group in security_groups_consolidated:
            security_group["HasResources"] = (
                "GroupId" in security_group
                and security_group["GroupId"] in used_security_groups_ids
            )
            security_groups.append(security_group)
        security_groups_consolidated = security_groups

        # VPC With Internet Access
        security_groups = []
        for security_group in security_groups_consolidated:
            vpc_id = security_group.get("VpcId")
            if vpc_id is None:
                security_group["HasInternetGateway"] = False
                security_groups.append(security_group)
                continue

            vpc = self.get_vpc(vpc_id)
            internet_gateways = vpc.internet_gateways.all()
            internet_gateways_count = sum(1 for _ in internet_gateways)
            security_group["HasInternetGateway"] = internet_gateways_count > 0
            security_groups.append(security_group)
        security_groups_consolidated = security_groups

        return security_groups_consolidated

    def get_regions(self):
        logger.info("Getting Regions")
        regions_dict_list = self.client.describe_regions()["Regions"]
        regions = [region["RegionName"] for region in regions_dict_list]
        return regions
