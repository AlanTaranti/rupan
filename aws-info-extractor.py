import os

import fire

from src.aws_account_service import AwsAccountService
from src.security_group_service import SecurityGroupService
from src.access_key_service import AccessKeyService
from src.bucket_service import BucketService
from src.logging_service import LoggingService


def get_filepath(module_name: str):
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)
    account_id = get_account_id()
    return os.path.join(base_dir, "{}_{}.csv".format(account_id, module_name))


def get_account_id():
    aws_service = AwsAccountService()
    return aws_service.get_account_id()


def aws_sg_extractor():
    """
    Um simples extrator de Security Groups da AWS
    """

    # Obter os security groups
    security_group_service = SecurityGroupService()

    # Obter Filepath
    filepath = get_filepath("security_group")

    # Obter dados
    dataframes = security_group_service.to_pandas()

    # Salvar Dados
    dataframes.to_csv(filepath, index=False)


def access_key_extractor():
    """
    Um simples extrator de Access Key da AWS
    """
    service = AccessKeyService()
    access_keys = service.get_access_keys()

    # Obter Filepath
    filepath = get_filepath("access_key")

    # Salvar Dados
    access_keys.to_csv(filepath, index=False)


def buckets_extractor():
    """
    Um simples extrator de Buckets da AWS
    """
    service = BucketService()
    buckets = service.get_buckets()

    # Obter Filepath
    filepath = get_filepath("buckets")

    # Salvar Dados
    buckets.to_csv(filepath, index=False)


def logging_extractor():
    """
    Um simples extrator de estado Logging da AWS
    """
    service = LoggingService()
    logging = service.get_logging()

    # Obter Filepath
    filepath = get_filepath("logging")

    # Salvar Dados
    logging.to_csv(filepath, index=False)


if __name__ == "__main__":
    fire.Fire(
        {
            "security-group": aws_sg_extractor,
            "access-keys": access_key_extractor,
            "buckets": buckets_extractor,
            "logging": logging_extractor,
        }
    )
