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
async def reservar(request: Request, nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    return f"""
    <html>
        <body>
            <h2>Reserva Confirmada</h2>
            <p>Gracias, {nombre}, tu reserva para el {fecha} a las {hora} ha sido confirmada.</p>
            <a href="/">Volver al inicio</a>
        </body>
    </html>
    """