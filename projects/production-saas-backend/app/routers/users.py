from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    EmailAlreadyRegisteredError,
    register_user,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return register_user(
            db=db,
            email=str(user_data.email).lower(),
            password=user_data.password,
        )
    except EmailAlreadyRegisteredError:
        raise HTTPException(
            status_code=409,
            detail="Email is already registered",
        )
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Could not register user because of a database constraint",
        )