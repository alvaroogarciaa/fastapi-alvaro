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

# Menú del restaurante
@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

# Página de reservas
@app.get("/reservas", response_class=HTMLResponse)
async def reservas(request: Request):
    return templates.TemplateResponse("reservas.html", {"request": request})

# Procesar la reserva
@app.post("/reservar", response_class=HTMLResponse)
async def reservar(request: Request):
    # Obtener los datos del formulario directamente
    form_data = await request.form()
    nombre = form_data.get('nombre')
    fecha = form_data.get('fecha')
    hora = form_data.get('hora')

    # Pasar los datos a la plantilla de confirmación
    return templates.TemplateResponse("reserva_confirmada.html", {
        "request": request, 
        "nombre": nombre, 
        "fecha": fecha, 
        "hora": hora
    })