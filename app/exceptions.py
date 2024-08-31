"""
This module contains custom exceptions and exception handlers for the FastAPI application.
"""
from typing import Any, Callable
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class CustomException(Exception):
    """
    Base exception class for all custom exceptions
    """


class InvalidAlgorithm(CustomException):
    """
    Exception raised when an invalid algorithm is provided.
    """


def create_exception_handler(status_code: int,
                             detail: Any,
                             headers: dict[str, str] | None = None) -> Callable[[Request, Exception], JSONResponse]:
    """
    Create an exception handler for a given status code and detail message.

    Args:
        status_code (int): The status code for the exception.
        detail (Any): The detail message for the exception.

    Returns:
        Callable[[Request, Exception], JSONResponse]: The exception handler function.
    """
    async def exception_handler(request: Request, exc: CustomException) -> JSONResponse:
        response_data = {"detail": detail}
        return JSONResponse(status_code=status_code, content=response_data, headers=headers)

    return exception_handler


def register_exception_handlers(app: FastAPI):
    """
    Registers exception handlers for the FastAPI application.
    """
    app.add_exception_handler(InvalidAlgorithm,
                              create_exception_handler(status.HTTP_400_BAD_REQUEST, "Invalid algorithm"))
