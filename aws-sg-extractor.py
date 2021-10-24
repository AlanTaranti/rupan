import fire
from src.security_group_service import SecurityGroupService


def AwsSgExtractor():
    service = SecurityGroupService()

    return service.get_security_groups()


def main():
    fire.Fire(AwsSgExtractor)


if __name__ == "__main__":
    main()
