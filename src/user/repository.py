from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from schemas import UserRead, UserCreate


class UserRepository(ABC):
    @abstractmethod
    def get_by_id_or_none(self, item_id: int) -> UserRead | None: ...

    @abstractmethod
    def get_by_username_or_none(self, name: str) -> UserRead | None: ...

    @abstractmethod
    def create_user(self, user: UserCreate) -> UserRead:
        pass


@dataclass
class UserRepositoryDict(UserRepository):
    storage: dict[int, dict] = field(default_factory=dict)

    def get_by_id_or_none(self, item_id: int):
        if item_id in self.storage:
            return UserRead(**self.storage[item_id] | {"id": item_id})
        return None

    def get_by_username_or_none(self, name: str):
        for key, value in self.storage.items():
            if value["username"] == name:
                return UserRead(**self.storage[key] | {"id": key})

    def create_user(self, user: UserCreate) -> UserRead:
        last_index = (
            list(self.storage.keys())[-1] + 1
            if len(list(self.storage.keys())) != 0
            else 1
        )
        self.storage[last_index] = user.model_dump()
        return UserRead(**user.model_dump() | {"id": last_index})


repo = UserRepositoryDict(
    {
        1: {"username": "vasia1", "password": "123"},
        2: {"username": "vasia2", "password": "123"},
        3: {"username": "vasia3", "password": "123"},
        4: {"username": "vasia4", "password": "123"},
        5: {"username": "vasia5", "password": "123"},
    }
)

# user = UserCreate(username='qweqwe', password='ewq')
# print(repo.create_user(user))
# print(repo.create_user(user))
# # print(repo.create_user(user))
# print(repo.storage)
