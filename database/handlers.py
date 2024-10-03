import traceback
from http import HTTPStatus

import structlog
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from repositories.exceptions import NotFoundError

logger = structlog.getLogger(__name__)


def _exc_to_str(exc: Exception) -> str:
    return "".join(traceback.format_exception(None, exc, exc.__traceback__))


def error_json_response(status: int, error: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status,
        content={
            "error": str(error),
        },
    )


async def request_validation_exception_handler(request: Request, exc: Exception) -> Response:
    logger.debug(
        "ошибка валидации запроса",
        error=exc,
        body=await request.body(),
        headers=request.headers,
    )
    return error_json_response(HTTPStatus.BAD_REQUEST, exc)


async def forbidden_exception_handler(request: Request, exc: Exception) -> Response:
    logger.debug(
        "ошибка авторизации",
        error=_exc_to_str(exc),
    )
    return error_json_response(HTTPStatus.FORBIDDEN, exc)


async def pydantic_validation_exception_handler(_: Request, exc: Exception) -> Response:
    logger.critical(
        "внутренняя ошибка валидации",
        error=_exc_to_str(exc),
    )
    return error_json_response(HTTPStatus.INTERNAL_SERVER_ERROR, exc)


async def internal_error_exception_handler(_: Request, exc: Exception) -> Response:
    logger.critical(
        "непредвиденная ошибка",
        error=_exc_to_str(exc),
    )
    return error_json_response(HTTPStatus.INTERNAL_SERVER_ERROR, exc)


async def not_found_error_exception_handler(_: Request, exc: Exception) -> Response:
    return error_json_response(HTTPStatus.BAD_REQUEST, exc)


def handle_exceptions(app: FastAPI) -> None:
    app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    app.add_exception_handler(ValidationError, pydantic_validation_exception_handler)
    app.add_exception_handler(NotFoundError, not_found_error_exception_handler)
    app.add_exception_handler(Exception, internal_error_exception_handler)
