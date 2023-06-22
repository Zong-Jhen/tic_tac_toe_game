# This is from the previous .py file because calling API are similar
# https://github.com/zxcqwe4906/python_backend_code_examples/blob/main/9_project1/template_example.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get(request: Request):
    return templates.TemplateResponse(
        "tic_tac_toe.html",
        {"request": request}
    )