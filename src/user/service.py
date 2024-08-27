from dataclasses import dataclass

from src.user.repository import UserRepository


@dataclass
class UserService:
    repository: UserRepository

    def get_by_username(self, name: str): ...

    def get_by_id(self, item_id: int): ...
