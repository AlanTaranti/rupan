from typing import List

from .base_repository import BaseRepository


class StsRepository(BaseRepository):
    @property
    def client(self):
        return self.session.client("sts")

    def get_account_id(self) -> str:
        return self.client.get_caller_identity()["Account"]
