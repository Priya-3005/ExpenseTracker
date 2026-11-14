from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import (
    ExpenseNotFoundException,
    UserNotFoundException,
    InvalidCredentialsException,
)

async def expense_not_found_handler(
    request: Request,
    exc: ExpenseNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.message
        }
    )
async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.message
        }
    )
async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):

    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": exc.message
        }
    )
async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error"
        }
    )