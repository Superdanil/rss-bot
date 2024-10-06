import uuid

from core.logger.log_handler import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class LoguruMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = str(uuid.uuid4())
        endpoint = self.get_endpoint_from_request(request)

        logger.info(
            "Входящий запрос", request_id=request_id, method=request.method, endpoint=endpoint, url=str(request.url),
        )

        response = await call_next(request)

        logger.info("Ответ сгенерирован", request_id=request_id, status_code=response.status_code)

        return response

    @staticmethod
    def get_endpoint_from_request(request: Request) -> str:
        return str(request.url).replace(str(request.base_url), "")
