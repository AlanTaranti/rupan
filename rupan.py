import fire


def list_inactive_lambdas(days: int = 180):
    """
    List and print inactive Lambda functions.

    Args:
        days (int): The number of days to check for inactivity.
    """

    from src.logger import logger
    from src.services.lambda_service import LambdaService

    logger.info("Extracting inactive Lambda functions")

    lambda_service = LambdaService()

    inactive_lambdas = lambda_service.list_inactive_lambdas(days)

    logger.info("Inactive Lambda functions:")
    for lambda_name in inactive_lambdas:
        print(lambda_name)


if __name__ == "__main__":
    fire.Fire(
        {
            "unused-lambda-functions": list_inactive_lambdas,
        }
    )
