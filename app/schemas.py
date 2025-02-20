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

    @validator("name")
    def validate_name(cls, name: str):
        """Ensure name contains only alphabetic characters and spaces."""
        if not re.match(r"^[A-Za-z\s]+$", name):
            raise ValueError("Name must contain only letters and spaces.")
        return name

    @validator("phone")
    def validate_phone(cls, phone: Optional[str]):
        """Ensure phone number is exactly 10 digits and starts with 6, 7, 8, or 9."""
        if phone is not None:
            if not re.match(r"^[6789]\d{9}$", phone):
                raise ValueError("Phone number must be exactly 10 digits and start with 6, 7, 8, or 9.")
        return phone

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
