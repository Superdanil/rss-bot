from typing import Annotated

from fastapi import Depends

from parser.repositories import UserRepository, OriginRepository

IUserRepository = Annotated[UserRepository, Depends(UserRepository)]
IOriginRepository = Annotated[OriginRepository, Depends(OriginRepository)]
