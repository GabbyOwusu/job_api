import fastapi
from fastapi import Depends, HTTPException
from src.dependencies.session import get_db
from src.repository.crud.job import JobCRUDRepository
from src.models.schemas.job import JobSchema, JobCreate, ApplicationSchema
from src.models.schemas.response_model import ResponseSchema
from src.utilities.jwt_generator import jwt_generator
from src.utilities.exceptions import EntityAlreadyExists
from uuid import UUID

router = fastapi.APIRouter(
    prefix='/jobs', tags=['Jobs'],
    dependencies=[Depends(jwt_generator.handle_token_authorization)]
)


def get_job_repo(db=Depends(get_db)):
    return JobCRUDRepository(db)


@router.get(
    '/user',
    response_model=ResponseSchema[list[JobSchema]],
    status_code=fastapi.status.HTTP_200_OK
)
def get_all_jobs(
    repo: JobCRUDRepository = Depends(get_job_repo),
    token: dict = Depends(jwt_generator.handle_token_authorization)
) -> list[JobSchema]:
    all_jobs = repo.get_jobs_by_user_id(user_id=token['user_id'])
    return ResponseSchema(
        status='sucess',
        message='Jobs fetched successfully',
        data=[JobSchema.model_validate(
            job, from_attributes=True) for job in all_jobs]
    )


@router.get(
    '/all',
    response_model=ResponseSchema[list[JobSchema]],
    status_code=fastapi.status.HTTP_200_OK
)
def get_all_jobs(
    repo: JobCRUDRepository = Depends(get_job_repo),
) -> list[JobSchema]:
    all_jobs = repo.get_all_jobs()
    return ResponseSchema(
        status='sucess',
        message='Jobs fetched successfully',
        data=[JobSchema.model_validate(
            job, from_attributes=True) for job in all_jobs]
    )


@router.post(
    '/create',
    response_model=ResponseSchema[JobSchema],
    status_code=fastapi.status.HTTP_200_OK,
)
def create_job(
    job: JobCreate,
    job_repo: JobCRUDRepository = Depends(get_job_repo),
    token: dict = Depends(jwt_generator.handle_token_authorization)
) -> ResponseSchema[JobSchema]:
    can_create = job_repo.can_create_job(user_id=token['user_id'])
    if can_create == False:
        raise HTTPException(status_code=403, detail='Operation not permitted')
    try:
        new_job = job_repo.create_job(user_id=token['user_id'], job=job)
        return ResponseSchema(
            status='success',
            message='Job created successfully',
            data=JobSchema.model_validate(new_job, from_attributes=True)
        )
    except:
        raise HTTPException(status_code=500, detail='Internal server error')


@router.post(
    "/{id}/apply",
    response_model=ResponseSchema[ApplicationSchema],
    status_code=fastapi.status.HTTP_201_CREATED
)
def apply_to_job(
    id: UUID,
    job_repo: JobCRUDRepository = Depends(get_job_repo),
    token: dict = Depends(jwt_generator.handle_token_authorization)
) -> ResponseSchema[ApplicationSchema]:
    try:
        application = job_repo.apply_to_job(
            job_id=id, user_id=token['user_id'],
        )
    except EntityAlreadyExists as error:
        raise HTTPException(status_code=400, detail=str(error))
    return ResponseSchema(
        status='success',
        message='You have successfully applied for this job',
        data=ApplicationSchema.model_validate(
            application, from_attributes=True
        )
    )
