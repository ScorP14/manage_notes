from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from src.user.schemas import UserRead, UserCreate


class UserRepository(ABC):
    @abstractmethod
    def get_by_id_or_none(self, item_id: int) -> UserRead | None: ...

    @abstractmethod
    def get_by_username_or_none(self, name: str) -> UserRead | None: ...

    @abstractmethod
    def create_user(self, user: UserCreate) -> UserRead: ...


def get_db_user():
    return {
        1: {"username": "user1", "password": "1"},
        2: {"username": "user2", "password": "2"},
        3: {"username": "user3", "password": "3"},
        4: {"username": "user4", "password": "4"},
        5: {"username": "user5", "password": "5"},
    }


@dataclass
class UserRepositoryDict(UserRepository):
    storage: dict[int, dict] = field(default_factory=get_db_user)

    def get_by_id_or_none(self, item_id: int) -> UserRead | None:
        if item_id in self.storage:
            return UserRead(**self.storage[item_id] | {"id": item_id})
        return None

    def get_by_username_or_none(self, name: str) -> UserRead | None:
        for key, value in self.storage.items():
            if value["username"] == name:
                return UserRead(**self.storage[key] | {"id": key})
        return None

    def create_user(self, user: UserCreate) -> UserRead:
        last_index = (
            list(self.storage.keys())[-1] + 1
            if len(list(self.storage.keys())) != 0
            else 1
        )
        self.storage[last_index] = user.model_dump()
        return UserRead(**user.model_dump() | {"id": last_index})
