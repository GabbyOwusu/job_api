
from src.models.schemas.response_model import ResponseSchema, ErrorSchema
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


class HTTPExceptionHandler:

    def __init__(self):
        # Map status codes to error codes
        self.status_code_to_error_code = {
            400: "BAD_REQUEST",
            401: "UNAUTHORIZED",
            403: "FORBIDDEN",
            404: "NOT_FOUND",
            409: "CONFLICT",
            422: "VALIDATION_ERROR",
            500: "INTERNAL_SERVER_ERROR",
        }

    def _get_error_code(self, status_code: int) -> str:
        """Get error code from status code"""
        return self.status_code_to_error_code.get(status_code, "ERROR")

    def _get_error_message(self, detail: str | dict) -> str:
        """Extract error message from detail (handles both string and dict)"""
        if isinstance(detail, dict):
            return detail.get("message", str(detail))
        return str(detail)

    async def __call__(self, request: Request, exc: HTTPException) -> JSONResponse:
        """
        Handle HTTPException and convert to ResponseSchema format
        """
        error_code = self._get_error_code(exc.status_code)
        error_message = self._get_error_message(exc.detail)

        error_response = ResponseSchema(
            status="error",
            message="An error occurred",
            data=None,
            error=ErrorSchema(
                message=error_message,
                code=error_code
            )
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=error_response.model_dump()
        )


http_exception_handler: HTTPExceptionHandler = HTTPExceptionHandler()


class EntityDoesNotExist(Exception):
    """
    Throw an exception when the data does not exist in the database.
    """


class EntityAlreadyExists(Exception):
    """
    Throw an exception when the data already exist in the database.
    """
