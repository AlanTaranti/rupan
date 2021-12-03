from .base_repository import BaseRepository


class IamRepository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("iam")

    @property
    def resource(self):
        return self.get_session().resource("iam")

    def get_access_key_last_used(self, access_key):
        return self.client.get_access_key_last_used(AccessKeyId=access_key)[
            "AccessKeyLastUsed"
        ]

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

        for key in keys:
            last_used_data = self.get_access_key_last_used(key["AccessKeyId"])
            key["LastUsedDate"] = last_used_data.get("LastUsedDate")
            key["ServiceName"] = last_used_data.get("ServiceName")
            key["Region"] = last_used_data.get("Region")

        return keys
