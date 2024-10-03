from typing import Annotated

from fastapi.params import Depends

from database.services import SourceService, UserService, NewsService

IUserService = Annotated[UserService, Depends(UserService)]
ISourceService = Annotated[SourceService, Depends(SourceService)]
INewsService = Annotated[NewsService, Depends(NewsService)]
