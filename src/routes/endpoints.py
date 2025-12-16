import fastapi
from src.routes.user import router as user_router
from src.routes.authentication import router as auth_router
from src.routes.jobs import router as jobs_router

endpoint_router = fastapi.APIRouter()


endpoint_router.include_router(router=user_router)
endpoint_router.include_router(router=auth_router)
endpoint_router.include_router(router=jobs_router)
