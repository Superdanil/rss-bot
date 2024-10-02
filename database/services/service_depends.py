from typing import Annotated

from fastapi import Depends

from ..repositories import UserRepository, OriginRepository, NewsRepository

IUserRepository = Annotated[UserRepository, Depends(UserRepository)]
IOriginRepository = Annotated[OriginRepository, Depends(OriginRepository)]
INewsRepository = Annotated[NewsRepository, Depends(NewsRepository)]
