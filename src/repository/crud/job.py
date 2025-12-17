from src.repository.crud.base import BaseCRUDRepository
from src.models.schemas.job import JobCreate
from src.models.db.job import Job
from src.models.db.user import User
from src.models.db.application import Application
from uuid import UUID
from src.utilities.exceptions import EntityAlreadyExists


class JobCRUDRepository(BaseCRUDRepository):

    def get_jobs_by_user_id(self, user_id: UUID) -> list[Job]:
        jobs = self.session.query(Job).where(Job.user_id == user_id)
        return jobs

    def get_all_jobs(self) -> list[Job]:
        jobs = self.session.query(Job).all()
        return jobs

    def create_job(self, user_id: UUID, job: JobCreate) -> Job:
        job_create = Job(
            title=job.title,
            description=job.description,
            user_id=user_id
        )
        self.session.add(job_create)
        self.session.commit()
        self.session.refresh(job_create)

        return job_create

    def can_create_job(self, user_id: UUID) -> bool:
        user = self.session.query(User).where(User.id == user_id).first()
        return user.user_type == 'employer'

    def apply_to_job(self, job_id: UUID, user_id: UUID) -> Application:
        existing_application = self.session.query(Application).where(
            Application.user_id == user_id,
            Application.job_id == job_id
        ).first()
        if existing_application is not None:
            raise EntityAlreadyExists('User already applied to job')
        new_application = Application(user_id=user_id, job_id=job_id)
        self.session.add(new_application)
        self.session.commit()
        self.session.refresh(new_application)
        return new_application

    def update_job(self):
        pass

    def delete_job(self):
        pass

    def get_job_applications(self):
        
        pass
