from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)
from dataclasses import dataclass, field
from typing import AsyncGenerator

from src.settings import get_settings


url = get_settings().database.get_url()


@dataclass
class DataBaseAsyncHelper:
    url: str
    is_echo: bool = field(default=False)

    def __post_init__(self):
        self.engine: AsyncEngine = create_async_engine(
            url=self.url,
            echo=self.is_echo,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


class BaseDataBase(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


db = DataBaseAsyncHelper(url, is_echo=True)
