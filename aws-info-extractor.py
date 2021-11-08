import os

import fire

from src.aws_account_service import AwsAccountService
from src.security_group_service import SecurityGroupService


def aws_sg_extractor():
    """
    Um simples extrator de Security Groups da AWS
    """

    # Obter os security groups
    security_group_service = SecurityGroupService()
    aws_service = AwsAccountService()

    # Criar diretorio de saida de arquivos
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, "{}.csv".format(aws_service.get_account_id()))

    dataframes = security_group_service.to_pandas()
    dataframes.to_csv(filepath, index=False)


if __name__ == "__main__":
    fire.Fire({
        'security-group': aws_sg_extractor
    })
