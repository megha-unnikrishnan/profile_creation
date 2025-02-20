



from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
     return {"message": "Profile Creation System API"}
