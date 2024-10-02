from typing import Annotated

from fastapi.params import Depends

from database.services import OriginService, UserService, NewsService

IUserService = Annotated[UserService, Depends(UserService)]
IOriginService = Annotated[OriginService, Depends(OriginService)]
INewsService = Annotated[NewsService, Depends(NewsService)]
