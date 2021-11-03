import os

import fire

from src.security_group_service import SecurityGroupService


def aws_sg_extractor(profile: str = "default"):
    """
    Um simples extrator de Security Groups da AWS
    """

    # Obter os security groups
    service = SecurityGroupService(profile=profile)

    # Criar diretorio de saida de arquivos
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, "{}.csv".format(profile))

    dataframes = service.to_pandas()
    dataframes.to_csv(filepath, index=False)


if __name__ == "__main__":
    fire.Fire(aws_sg_extractor)
