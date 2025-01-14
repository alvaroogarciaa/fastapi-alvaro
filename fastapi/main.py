from typing import Union

from fastapi import FastAPI, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

@app.get("/menu/entrantes", response_class=HTMLResponse)
async def entradas(request: Request):
    return templates.TemplateResponse("entrantes.html", {"request": request})

@app.get("/menu/platos-principales", response_class=HTMLResponse)
async def platos_principales(request: Request):
    return templates.TemplateResponse("platos_principales.html", {"request": request})

@app.get("/menu/postres", response_class=HTMLResponse)
async def postres(request: Request):
    return templates.TemplateResponse("postres.html", {"request": request})

@app.get("/menu/bebidas", response_class=HTMLResponse)
async def bebidas(request: Request):
    return templates.TemplateResponse("bebidas.html", {"request": request})

@app.get("/menu/menu-infantil", response_class=HTMLResponse)
async def menu_infantil(request: Request):
    return templates.TemplateResponse("menu_infantil.html", {"request": request})

@app.get("/reservas", response_class=HTMLResponse)
async def reservas(request: Request):
    return templates.TemplateResponse("reservas.html", {"request": request})

@app.post("/reservar", response_class=HTMLResponse)
async def reservar(request: Request, nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    return templates.TemplateResponse("confirmacion.html", {"request": request, "nombre": nombre, "fecha": fecha, "hora": hora})