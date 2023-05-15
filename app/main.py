import os
from fastapi import FastAPI

from initial_data import main
from starlette.middleware.cors import CORSMiddleware

from controllers.routers import api_router
from core.config import settings



app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description=f"{settings.DESCRIPTION_FOR_FIRST_USE_OF_API,settings.FIRST_SUPERUSER,settings.FIRST_SUPERUSER_PASSWORD}"
    )
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        
    )

main()

app.include_router(api_router, prefix=settings.API_V1_STR)
