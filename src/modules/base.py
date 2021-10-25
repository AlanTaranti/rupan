from typing import List


class BaseModule:
    def get_segurity_groups(self) -> List:
        raise NotImplementedError()
