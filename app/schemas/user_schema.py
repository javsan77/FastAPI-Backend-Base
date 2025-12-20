from pydantic import BaseModel, EmailStr, Field

#---------------------------------
# Schema to Create User
#---------------------------------
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr

#---------------------------------
# Schema to Create User
#---------------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr