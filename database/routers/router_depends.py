from typing import Annotated

from fastapi.params import Depends

from database.repositories import IDBHelper
from database.services.news_service import NewsService
from database.services.source_service import SourceService
from database.services.user_service import UserService
from database.services.user_source_service import UserInteractor

IUserService = Annotated[UserService, Depends(UserService)]
ISourceService = Annotated[SourceService, Depends(SourceService)]
INewsService = Annotated[NewsService, Depends(NewsService)]


def get_user_interactor(user_service: IUserService, source_service: ISourceService, db_helper: IDBHelper):
    return UserInteractor(user_service=user_service, source_service=source_service, db_helper=db_helper)
