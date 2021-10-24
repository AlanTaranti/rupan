from typing import List, Dict

from .modules.base import BaseModule
from .modules.ec2 import Ec2
from .modules.rds import Rds
from .modules.redshift import Redshift
from .modules.elasticache import Elasticache


class SecurityGroupService:
    @property
    def modules(self) -> Dict[str, BaseModule]:
        return {
            "ec2": Ec2,
            "rds": Rds,
            "redshift": Redshift,
            "elasticache": Elasticache,
        }

    def get_security_groups(self) -> List:
        security_groups = {}
        for module_name, module_class in self.modules.items():
            module_instance = module_class()
            security_groups[module_name] = module_instance.get_segurity_groups()

        return security_groups
