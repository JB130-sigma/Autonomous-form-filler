from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, LoginRequest
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def register(db: Session, request: RegisterRequest):

        existing_user = UserRepository.get_by_email(
            db,
            request.email,
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        hashed_password = hash_password(
            request.password
        )

        user = User(
            username=request.username,
            email=request.email,
            password_hash=hashed_password,
        )

        return UserRepository.create(
            db,
            user,
        )

    @staticmethod
    def login(db: Session, request: LoginRequest):

        user = UserRepository.get_by_email(
            db,
            request.email,
        )

        if not user:
            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }