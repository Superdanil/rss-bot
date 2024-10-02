from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from parser.core.models import db_helper

IAsyncSession = Annotated[AsyncSession, Depends(db_helper.session_getter)]
