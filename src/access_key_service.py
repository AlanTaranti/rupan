from .repository.iam_repository import IamRepository


class AccessKeyService:
    def get_access_keys(self):
        repository = IamRepository()
        return repository.list_access_keys()
