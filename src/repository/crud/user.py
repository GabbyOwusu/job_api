from src.repository.crud.base import BaseCRUDRepository
from uuid import UUID
from src.models.db.user import User
from src.models.schemas.user import UserCreate
from src.utilities.exceptions import EntityAlreadyExists
from src.utilities.hash_generator import hash_generator


class UserCRUDRepository(BaseCRUDRepository):

    def find_user_by_email(self, email: str) -> User:
        user = self.session.query(User).where(User.email == email).first()
        print(f'User exists {user}')
        if user is not None:
            raise EntityAlreadyExists("Email already exists")
        return user

    def create_user(self, user: UserCreate) -> User:
        password_hash = hash_generator.hash_password(user.password)
        new_account = User(email=user.email, password=password_hash)
        self.session.add(instance=new_account)
        self.session.commit()
        self.session.refresh(new_account)

        return new_account

    def get_all_users(self):
        users = self.session.query(User).all()
        return users
