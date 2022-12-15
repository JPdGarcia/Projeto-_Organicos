from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from uvicorn import run

from database import db_router
from routes import router


app = FastAPI()

@app.get("/", response_class=RedirectResponse, tags=["Index"])
def index():
    return "/docs"

app.include_router(router)
app.include_router(db_router)

if __name__ == "__main__":
    run("app:app", reload=True)