import fire
from src.security_group_service import SecurityGroupService


def AwsSgExtractor():
    """
    Um simples extrator de Security Groups da AWS
    """
    service = SecurityGroupService()

    return service.get_security_groups()


if __name__ == "__main__":
    fire.Fire(AwsSgExtractor)
