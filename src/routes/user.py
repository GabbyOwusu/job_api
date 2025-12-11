import fastapi
from fastapi import Depends, HTTPException
from src.dependencies.session import get_db
from src.repository.crud.user import UserCRUDRepository
from src.models.schemas.response_model import ResponseSchema
from src.models.schemas.user import UserSchema

router = fastapi.APIRouter(
    prefix='/user',
    tags=['User']
)


def get_user_repo(db=Depends(get_db)):
    return UserCRUDRepository(db)


@router.get(
    "/all",
    response_model=ResponseSchema[list[UserSchema]],
    status_code=fastapi.status.HTTP_200_OK
)
def get_all_users(repo: UserCRUDRepository = Depends(get_user_repo)) -> ResponseSchema[list[UserSchema]]:
    users = repo.get_all_users()
    return ResponseSchema(
        status='success',
        message='Users fetched successfully',
        data=[UserSchema.model_validate(
            user, from_attributes=True) for user in users]
    )
