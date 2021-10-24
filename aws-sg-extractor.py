import fire
import pandas as pd

from src.security_group_service import SecurityGroupService


def AwsSgExtractor():
    """
    Um simples extrator de Security Groups da AWS
    """
    service = SecurityGroupService()

    security_groups = service.get_security_groups()
    dataframe = pd.DataFrame(security_groups)

    dataframe.to_csv("security_groups.csv")


if __name__ == "__main__":
    fire.Fire(AwsSgExtractor)
