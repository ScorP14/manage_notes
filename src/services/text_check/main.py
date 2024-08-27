from dataclasses import dataclass
from pyaspeller import YandexSpeller

from src.services.text_check.base import CheckText


@dataclass
class CheckTextYandexSpeller(CheckText):
    def __post_init__(self) -> None:
        self._api_client = YandexSpeller()

    def execute(self) -> str:
        return self._api_client.spelled(self.text)
