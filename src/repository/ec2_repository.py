from typing import List

from .base_repository import BaseRepository


class Ec2Repository(BaseRepository):
    @property
    def client(self):
        return self.session.client("ec2")

    @property
    def resource(self):
        return self.session.resource("ec2")

    def get_all_ec2_instances(self):
        return self.resource.instances.all()

    def get_all_ec2_security_groups_ids(self):
        instances = self.get_all_ec2_instances()

        security_groups_ids = []
        for instance in instances:
            security_groups = instance.security_groups
            if security_groups is not None:
                for security_group in security_groups:
                    security_groups_ids.append(security_group["GroupId"])

        return list(set(security_groups_ids))

    def get_vpc(self, id: str):
        return self.resource.Vpc(id)

    def get_segurity_groups(self) -> List:
        used_security_groups_ids = self.get_all_ec2_security_groups_ids()
        secrity_groups = self.client.describe_security_groups()["SecurityGroups"]
        secrity_groups_consolidated = []

        for security_group in secrity_groups:
            security_group["HasResources"] = (
                "GroupId" in security_group
                and security_group["GroupId"] in used_security_groups_ids
            )
            secrity_groups_consolidated.append(security_group)

        return secrity_groups_consolidated

    def get_regions(self):
        regions_dict_list = self.client.describe_regions()["Regions"]
        regions = [region["RegionName"] for region in regions_dict_list]
        return regions
