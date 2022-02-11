"""
Base Pydantic Object for Containers
"""

from pydantic import BaseModel


class MLServerModel(BaseModel):
    """
    MLServer Pydantic BaseModel
    """


class HashableMLServerModel(MLServerModel):
    """
    Hashable MLServerModel
    """

    def __hash__(self) -> int:
        """
        Hash Method for Pydantic BaseModels
        """
        return hash((type(self),) + tuple(self.__dict__.values()))
