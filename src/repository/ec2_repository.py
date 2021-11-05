from typing import List

from .base_repository import BaseRepository


class Ec2Repository(BaseRepository):
    @property
    def client(self):
        return self.session.client("ec2")

    def get_segurity_groups(self) -> List:
        return self.client.describe_security_groups()["SecurityGroups"]

    def get_regions(self):
        regions_dict_list = self.client.describe_regions()["Regions"]
        regions = [region["RegionName"] for region in regions_dict_list]
        return regions
