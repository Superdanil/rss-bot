from typing import Annotated

from fastapi.params import Depends

from parser.services import OriginService, UserService

IOriginService = Annotated[OriginService, Depends(OriginService)]
IUserService = Annotated[UserService, Depends(UserService)]
