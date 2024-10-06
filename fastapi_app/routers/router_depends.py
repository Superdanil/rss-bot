from typing import Annotated

from fastapi.params import Depends

from repositories import IDBHelper
from services.news_service import NewsService
from services.source_service import SourceService
from services.user_service import UserService
from services.user_source_service import UserInteractor

IUserService = Annotated[UserService, Depends(UserService)]
ISourceService = Annotated[SourceService, Depends(SourceService)]
INewsService = Annotated[NewsService, Depends(NewsService)]


def get_user_interactor(user_service: IUserService, source_service: ISourceService, db_helper: IDBHelper):
    return UserInteractor(user_service=user_service, source_service=source_service, db_helper=db_helper)
