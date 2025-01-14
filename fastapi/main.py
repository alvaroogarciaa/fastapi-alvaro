from typing import Union

from fastapi import FastAPI, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/frutas", response_class=HTMLResponse)
async def frutas(request: Request):
    return templates.TemplateResponse("frutas.html", {"request": request})

@app.get("/pescado-marisco", response_class=HTMLResponse)
async def pescado(request: Request):
    return templates.TemplateResponse("pescados-mariscos.html", {"request": request})

@app.get("/alcohol", response_class=HTMLResponse)
async def alcohol(request: Request):
    return templates.TemplateResponse("alcoholes.html", {"request": request})

@app.get("/lacteos", response_class=HTMLResponse)
async def lacteos(request: Request):
    return templates.TemplateResponse("lacteos.html", {"request": request})