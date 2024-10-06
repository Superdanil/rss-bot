from typing import Annotated

from fastapi import Depends

from repositories import UserRepository, SourceRepository, NewsRepository
from repositories import UserSourceAssociationRepository

IUserRepository = Annotated[UserRepository, Depends(UserRepository)]
ISourceRepository = Annotated[SourceRepository, Depends(SourceRepository)]
IUserSourceAssociationRepository = Annotated[UserSourceAssociationRepository, Depends(UserSourceAssociationRepository)]
INewsRepository = Annotated[NewsRepository, Depends(NewsRepository)]
