from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import StudentProfile
from .schemas import StudentCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-profile/")
def create_profile(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = StudentProfile(
        name=student.name,
        email=student.email,
        phone=student.phone,
        password=student.password  # No hashing
    )
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": "Profile created successfully", "student": student}
