from .base_repository import BaseRepository


class IamRepository(BaseRepository):
    @property
    def client(self):
        return self.session.client("iam")

    @property
    def resource(self):
        return self.session.resource("iam")

    def list_users(self):
        return self.resource.users.all()

    def list_user_access_keys(self, username):
        return self.client.list_access_keys(UserName=username)["AccessKeyMetadata"]

    def list_access_keys(self) -> str:
        users = self.list_users()

        keys = []

        for user in users:
            user_keys = self.list_user_access_keys(user.user_name)
            keys.extend(user_keys)

        return keys
