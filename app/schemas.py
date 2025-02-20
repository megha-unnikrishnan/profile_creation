



# from pydantic import BaseModel, EmailStr, Field, validator
# import re
# from typing import Optional

# class StudentCreate(BaseModel):
#     name: str
#     email: EmailStr
#     phone: Optional[str] = None
#     password: str = Field(..., min_length=8)

#     @validator("password")
#     def validate_password(cls, password: str):
#         """Ensure password meets security criteria."""
#         if len(password) < 8:
#             raise ValueError("Password must be at least 8 characters long.")
#         if not any(char.isupper() for char in password):
#             raise ValueError("Password must contain at least one uppercase letter.")
#         if not any(char.islower() for char in password):
#             raise ValueError("Password must contain at least one lowercase letter.")
#         if not any(char.isdigit() for char in password):
#             raise ValueError("Password must contain at least one numeric digit.")
#         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#             raise ValueError("Password must contain at least one special character.")
#         return password

#     class Config:
#         orm_mode = True




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, ValidationError, validator
import re
from typing import Optional

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    password: str = Field(..., min_length=8)

    @validator("password")
    def validate_password(cls, password: str):
        """Ensure password meets security criteria."""
        errors = []
        if len(password) < 8:
            errors.append("Must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            errors.append("Must contain at least one uppercase letter (A-Z)")
        if not any(char.islower() for char in password):
            errors.append("Must contain at least one lowercase letter (a-z)")
        if not any(char.isdigit() for char in password):
            errors.append("Must include at least one numeric digit (0-9)")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            errors.append("Must include at least one special character (e.g., @, #, $, %)")
        
        if errors:
            raise ValueError("; ".join(errors))  # Raise all errors at once
        
        return password

    class Config:
        orm_mode = True

@app.post("/register")
async def register_student(student: StudentCreate):
    try:
        return {
            "message": "Profile created successfully!",
            "profile_details": {
                "name": student.name,
                "email": student.email,
                "phone": student.phone,
            }
        }
    except ValidationError as e:
        error_details = []
        for error in e.errors():
            if error["loc"][0] == "password":
                error_details.append(error["msg"])
        
        raise HTTPException(
            status_code=422,
            detail={
                "error": "Password does not meet policy requirements",
                "details": error_details
            }
        )

