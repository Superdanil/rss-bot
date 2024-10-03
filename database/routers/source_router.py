from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from database.core.dtos.source_dto import SourceDTO
from database.routers.router_depends import ISourceService

router = APIRouter(prefix="/sources", tags=["sources"])


# @router.get("", response_model=list[SourceDTO])
# async def get_users_sources(service: ISourceService, dto: SourceDTO):
#     """Возвращает список подписок пользователя."""
#     try:
#         return await service.get_users_sources(dto=dto)
#     except AlreadyExistError as e:
#         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("", status_code=HTTP_200_OK)
async def create_source(service: ISourceService, dto: SourceDTO) -> JSONResponse:
    """Эндпоинт регистрации источника новостей"""

    await service.add_or_get_source(dto=dto)
    return JSONResponse("Источник успешно добавлен")
