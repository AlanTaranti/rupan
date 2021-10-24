from typing import List, Dict
import importlib

from .modules.base import BaseModule


class SecurityGroupService:
    @property
    def modules_config(self) -> List[Dict[str, str]]:
        return [
            {
                "module": "ec2",
                "class": "Ec2",
            },
            {
                "module": "rds",
                "class": "Rds",
            },
            {
                "module": "redshift",
                "class": "Redshift",
            },
        ]

    @property
    def modules(self) -> Dict[str, BaseModule]:
        module_dict = {}

        for module_config in self.modules_config:
            module_name = module_config["module"]
            module = importlib.import_module(".modules.{}".format(module_name), "src")
            module_dict[module_name] = getattr(module, module_config["class"])

        return module_dict

    def get_security_groups(self) -> List:
        security_groups = {}
        for module_name, module_class in self.modules.items():
            module_instance = module_class()
            security_groups[module_name] = module_instance.get_segurity_groups()

        return security_groups
