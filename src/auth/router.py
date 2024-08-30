from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import Annotated

from jwt import InvalidTokenError

from src.auth.dependencies import (
    authenticate_user,
    create_token,
)
from src.auth.schemas import Token, TokenData
from src.auth.dependencies import decode_token
from src.user.repository import UserRepository
from src.user.dependencies import get_user_repository
from src.user.schemas import UserRead

router = APIRouter(tags=["auth"])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось проверить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username: str = decode_token(token).get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = user_repository.get_by_username_or_none(token_data.username)
    if user is None:
        raise credentials_exception
    return user


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> Token:
    user = authenticate_user(user_repository, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me", response_model=UserRead)
async def read_users_me(
    current_user: Annotated[UserRead, Depends(get_current_user)],
):
    return current_user
