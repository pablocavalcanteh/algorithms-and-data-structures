from abc import ABC, abstractmethod
from typing import List

class ISorting(ABC):

    vector: List

    def __init__(self, vector):
        self.vector = vector

    @abstractmethod
    def sort(self) -> None:
        raise NotImplementedError