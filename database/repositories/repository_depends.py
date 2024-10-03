from typing import Annotated

from fastapi import Depends

from database.core.models import DatabaseHelper
from database.core.settings import settings
from database.repositories.source_repository import SourceRepository

IDBHelper = Annotated[DatabaseHelper, Depends(lambda: DatabaseHelper(url=str(settings.DB_URL)))]
ISourceRepository = Annotated[SourceRepository, Depends(SourceRepository)]
