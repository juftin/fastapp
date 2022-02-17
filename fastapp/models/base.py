"""
Base Pydantic Object for Containers
"""

from pydantic import BaseModel


class FastAppModel(BaseModel):
    """
    FastApp Pydantic BaseModel
    """


class HashableFastAppModel(FastAppModel):
    """
    Hashable FastAppModel
    """

    def __hash__(self) -> int:
        """
        Hash Method for Pydantic BaseModels
        """
        return hash((type(self),) + tuple(self.__dict__.values()))
