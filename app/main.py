from fastapi import FastAPI
from pydantic import BaseModel, AnyHttpUrl

app = FastAPI()


class URLCreate(BaseModel):
    url: AnyHttpUrl


@app.get("/")
def root():
    return {"message": "URL Shortener"}


@app.post("/urls", status_code=201)
def create_url(data: URLCreate):
    return {
        "url": data.url
    }