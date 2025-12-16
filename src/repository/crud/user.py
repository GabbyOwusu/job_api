from src.repository.crud.base import BaseCRUDRepository
from uuid import UUID
from src.models.db.user import User
from src.models.schemas.user import UserCreate
from src.utilities.exceptions import EntityAlreadyExists, EntityDoesNotExist, InvalidCredentials
from src.utilities.hash_generator import hash_generator


class UserCRUDRepository(BaseCRUDRepository):

    def find_user_by_email(self, email: str) -> User:
        user = self.session.query(User).where(User.email == email).first()
        if user is not None:
            raise EntityAlreadyExists("Email already exists")
        return user

    def authenticate_user_email(self, email: str) -> User:
        user = self.session.query(User).where(User.email == email).first()
        if user is None:
            raise EntityDoesNotExist("Invalid credentials")
        return user

    def find_user_by_id(self, id: str) -> User:
        user = self.session.query(User).where(User.id == id).first()
        if user is None:
            raise EntityAlreadyExists(f"User with id {id} does not exist")
        return user

    def authenticate_with_email_password(self, email: str, password: str) -> User:
        user = self.session.query(User).where(User.email == email).first()

        if user is None:
            raise InvalidCredentials('Invalid credentials')
        is_valid_password = hash_generator.verify_hash_password(
            password=password,
            hashed_password=user.password
        )
        if not is_valid_password:
            raise InvalidCredentials('Wrong password')
        return user

    def create_user(self, user: UserCreate) -> User:
        password_hash = hash_generator.hash_password(user.password)
        new_account = User(
            email=user.email,
            password=password_hash,
            first_name=user.first_name,
            last_name=user.last_name,
            user_type=user.user_type
        )
        self.session.add(instance=new_account)
        self.session.commit()
        self.session.refresh(new_account)

        return new_account

    def get_all_users(self):
        users = self.session.query(User).all()
        return users
