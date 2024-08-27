from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CheckText(ABC):
    text: str

    @abstractmethod
    def execute(self) -> str: ...
