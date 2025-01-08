from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.schemas_user import UserCreate, User

router = APIRouter(
    prefix="/authorization",
    tags=["authorization"]
)

fake_users_db = {
    "johndoe": {
        "name": "John",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "fakehashedpassword",
        "workstation": "Student",
        "disabled": False,
    },
    "alice": {
        "name": "Alice",
        "username": "alice",
        "email": "alice@example.com",
        "password": "fakehashedsecret2",
        "workstation": "PhD",
        "disabled": True,
    },
}


def fake_has_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authorization/token")


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserCreate(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserCreate(**user_dict)
    hashed_password = fake_has_password(form_data.password)
    print(hashed_password, user.password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
