from typing import Annotated

from fastapi import Depends

from core.models import DatabaseHelper
from core.settings import settings
from repositories.source_repository import SourceRepository

IDBHelper = Annotated[DatabaseHelper, Depends(lambda: DatabaseHelper(url=str(settings.DB_URL)))]
ISourceRepository = Annotated[SourceRepository, Depends(SourceRepository)]
