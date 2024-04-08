# api/main.py

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

# Define your custom exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Custom exception handler to handle HTTPExceptions.
    """
    return {"detail": f"An error occurred: {exc.detail}"}

# Import and include the router from development.py
from . import development
app.include_router(development.router)



