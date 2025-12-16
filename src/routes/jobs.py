import fastapi
from fastapi import Depends, HTTPException
from src.dependencies.session import get_db
from src.repository.crud.job import JobCRUDRepository
from src.models.schemas.job import JobSchema, JobCreate
from src.models.schemas.response_model import ResponseSchema
from src.utilities.jwt_generator import jwt_generator

router = fastapi.APIRouter(
    prefix='/jobs', tags=['Jobs'],
    dependencies=[Depends(jwt_generator.handle_token_authorization)]
)


def get_job_repo(db=Depends(get_db)):
    return JobCRUDRepository(db)


@router.get(
    '/all',
    response_model=ResponseSchema[list[JobSchema]],
    status_code=fastapi.status.HTTP_200_OK
)
def get_all_jobs(
    repo: JobCRUDRepository = Depends(get_job_repo),
    token: dict = Depends(jwt_generator.handle_token_authorization)
) -> list[JobSchema]:
    all_jobs = repo.get_all_jobs(user_id=token['user_id'])
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
    try:
        new_job = job_repo.create_job(user_id=token['user_id'], job=job)
        return ResponseSchema(
            status='success',
            message='Job created successfully',
            data=JobSchema.model_validate(new_job, from_attributes=True)
        )
    except:
        raise HTTPException(status_code=500, detail='Internal server error')
