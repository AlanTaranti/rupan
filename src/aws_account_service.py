from .repository.sts_repository import StsRepository


class AwsAccountService:
    def get_account_id(self):
        service = StsRepository()
        return service.get_account_id()
