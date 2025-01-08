from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    username: str
    email: str
    workstation: str
    disabled: bool


class UserCreate(UserBase):
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jan",
                "username": "kowalski",
                "email": "kowalski@sample.com",
                "password": "Password123@",
                "workstation": "Student/PhD/Academic Worker/Professor/Other"
            }
        }


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
