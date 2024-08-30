from datetime import timedelta, datetime, timezone

import jwt

from src.settings import get_settings
from src.user.repository import UserRepository


key_for_jwt_env = get_settings().jwt.secret_key
algorithms_env = get_settings().jwt.algorithm


def authenticate_user(repo: UserRepository, username: str, password: str):
    user = repo.get_by_username_or_none(username)
    if not user:
        return False
    if not user.password == password:
        return False
    return user


def decode_token(
    token: str,
    secret_key: str = key_for_jwt_env,
    algorithms: str = algorithms_env,
) -> dict:
    payload = jwt.decode(token, secret_key, algorithms=[algorithms])
    return payload


def create_token(
    data: dict,
    expires_delta: timedelta | None = None,
    secret_key: str = key_for_jwt_env,
    algorithms: str = algorithms_env,
) -> str:
    now_time = datetime.now(timezone.utc)
    expire = (
        now_time + expires_delta if expires_delta else now_time + timedelta(minutes=15)
    )
    encoded_jwt = jwt.encode(data | {"exp": expire}, secret_key, algorithm=algorithms)
    return encoded_jwt
