from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED

import parser.crud.users as users_crud
from parser.core.models import db_helper
from parser.core.schemas import UserCreate

router = APIRouter(prefix="/users")


@router.get("", response_model=list[UserCreate])
async def get_users(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    users = await users_crud.get_all_users(session=session)
    return users


@router.post("", response_model=UserCreate, status_code=HTTP_201_CREATED)
async def create_user(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], user_create: UserCreate):
    user = await users_crud.create_user(session=session, user_create=user_create)
    return user
