from fastapi import APIRouter, \
    Depends, \
    HTTPException
from sqlalchemy.orm import Session
from dependency import get_db
from functions.functions_user import create_user, \
    get_users, \
    get_user, \
    get_user_by_email, \
    delete_user
from schemas.schemas_user import UserCreate, \
    User
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
def read_users(db: Session = Depends(get_db)):
    """
    Get all users from database
    """
    users = get_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="There are no users in database")
    return users


@router.get("/{user_id}", response_model=User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Get user by ID
    - **user_id**: user ID
    """
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Add user to database
    - **email**: user email
    - **name**: user first name
    - **password**: password for account
    - **username**: user username
    - **workstation**: user workstation (Student/PhD/Academic Worker/Professor/Other)
    """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.delete("/{user_id}")
def delete_users(user_id: int, db: Session = Depends(get_db)):
    """
    Delete user by ID
    - **user_id**: user ID
    """
    return delete_user(db, user_id) # add raise exception
