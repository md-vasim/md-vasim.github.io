from fastapi import FastAPI, Request, Form, UploadFile, File, Depends, HTTPException, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import uvicorn 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})
