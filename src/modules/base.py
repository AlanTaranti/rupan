from typing import List


class BaseModule:
    def get_segurity_groups() -> List:
        raise NotImplementedError()
