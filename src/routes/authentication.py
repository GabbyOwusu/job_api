import fastapi
from fastapi import Depends
from fastapi import HTTPException

from src.models.schemas.user import UserCreate, UserSchema, UserWithTokenSchema, UserLogin
from src.models.schemas.response_model import ResponseSchema
from src.dependencies.session import get_db
from src.repository.crud.user import UserCRUDRepository
from src.utilities.exceptions import EntityAlreadyExists, InvalidCredentials
from src.utilities.jwt_generator import jwt_generator

router = fastapi.APIRouter(prefix='/auth', tags=['Auth'])


def get_user_repo(db=Depends(get_db)):
    return UserCRUDRepository(db)


@router.post(
    "/signup",
    response_model=ResponseSchema[UserWithTokenSchema],
    status_code=fastapi.status.HTTP_201_CREATED
)
def signup(
    user: UserCreate,
    user_repo: UserCRUDRepository = Depends(get_user_repo)
) -> ResponseSchema[UserWithTokenSchema]:

    try:
        user_repo.find_user_by_email(user.email)
    except EntityAlreadyExists as error:
        raise HTTPException(status_code=400, detail=str(error))
    new_user = user_repo.create_user(user)
    jwt_token = jwt_generator.create_access_token(
        data={'user_id': str(new_user.id)}
    )

    return ResponseSchema(
        status='success',
        message='User created successfully',
        data=UserWithTokenSchema(
            token=jwt_token,
            user=UserSchema.model_validate(new_user, from_attributes=True)
        )
    )


@router.post(
    "/login",
    response_model=ResponseSchema[UserWithTokenSchema],
    status_code=fastapi.status.HTTP_200_OK
)
def login(
    user: UserLogin,
    user_repo: UserCRUDRepository = Depends(get_user_repo)
) -> ResponseSchema[UserWithTokenSchema]:

    try:
        user = user_repo.authenticate_with_email_password(
            email=user.email,
            password=user.password
        )
    except EntityAlreadyExists as error:
        raise HTTPException(status_code=400, detail=str(error))
    except InvalidCredentials as error:
        raise HTTPException(status_code=400, detail=str(error))
    jwt_token = jwt_generator.create_access_token(
        data={'user_id': str(user.id)}
    )

    return ResponseSchema(
        status='success',
        message='User created successfully',
        data=UserWithTokenSchema(
            token=jwt_token,
            user=UserSchema.model_validate(user, from_attributes=True)
        )
    )
