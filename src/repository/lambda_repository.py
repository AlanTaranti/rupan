from .base_repository import BaseRepository


class LambdaRepository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("lambda")

    def get_paginator(self):
        return self.client.get_paginator('list_functions')
