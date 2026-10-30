from fastapi import FastAPI
from routes.stu_route import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Student CRUD API is running"
    }

