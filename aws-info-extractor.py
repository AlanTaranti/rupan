import os

import fire


def get_filepath(module_name: str):
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)
    account_id = get_account_id()
    return os.path.join(base_dir, "{}_{}.csv".format(account_id, module_name))


def get_account_id():
    from src.aws_account_service import AwsAccountService

    aws_service = AwsAccountService()
    return aws_service.get_account_id()


def aws_sg_extractor(silent=False, verbose=False):
    """
    Um simples extrator de Security Groups da AWS
    """

    os.environ["AWS_INFO_EXTRACTOR_SILENT"] = str(silent)
    os.environ["AWS_INFO_EXTRACTOR_VERBOSE"] = str(verbose)

    from src.logger import logger
    from src.security_group_service import SecurityGroupService

    logger.info("Starting Security Group Module")

    # Obter os security groups
    security_group_service = SecurityGroupService()

    # Obter Filepath
    filepath = get_filepath("security_group")

    # Obter dados
    dataframes = security_group_service.to_pandas()

    # Salvar Dados
    logger.info("Saving Data")
    dataframes.to_csv(filepath, index=False)


def access_key_extractor():
    """
    Um simples extrator de Access Key da AWS
    """

    from src.access_key_service import AccessKeyService

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
    from src.bucket_service import BucketService

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
    from src.logging_service import LoggingService

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
