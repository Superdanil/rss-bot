from typing import Annotated

from fastapi import Depends

from database.core.models import DatabaseHelper
from database.core.settings import settings

IDBHelper = Annotated[DatabaseHelper, Depends(lambda: DatabaseHelper(url=str(settings.DB_URL)))]
