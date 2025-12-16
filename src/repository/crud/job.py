from src.repository.crud.base import BaseCRUDRepository
from src.models.schemas.job import JobCreate
from src.models.db.job import Job
from uuid import UUID


class JobCRUDRepository(BaseCRUDRepository):

    def get_all_jobs(self, user_id: UUID) -> list[Job]:
        jobs = self.session.query(Job).where(Job.user_id == user_id)
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

    def update_job(self):
        pass

    def delete_job(self):
        pass

    def apply_to_job(self):
        pass

    def get_job_applications(self):
        pass
