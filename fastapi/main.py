from data.database import database
from typing import Annotated

from data.dao.dao_clientes import DaoClientes

from data.modelo.cliente import Cliente

from typing import Union

from fastapi import FastAPI, Request, Form

from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


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




@app.get("/")
def read_root():
    return DaoClientes().get_all(database)

@app.get("/clientes")
def get_clientes(request: Request, nombre: str = "nombre"):
    clientes = DaoClientes().get_all(database)
    return templates.TemplateResponse(
        "clientes.html", 
        {"request": request, "clientes": clientes}
    )

@app.post("/clientes/add")
async def add_clientes(request: Request, nombre: str = Form(...)):
    dao = DaoClientes()
    cliente = Cliente(id=None, nombre=nombre)  
    dao.add(database, cliente)
    
    return RedirectResponse(url="/clientes", status_code=303)


class ClienteDelete(BaseModel):
    nombre: str

@app.post("/clientes/delete")
def delete_clientes(request: Request, nombre: str = Form(...)):  
    dao = DaoClientes()
    
    dao.delete(database, nombre)
    
    clientes = dao.get_all(database)

    return templates.TemplateResponse(
        "clientes.html", 
        {"request": request, "clientes": clientes, "message": f"Cliente '{nombre}' eliminado correctamente"}
    )

@app.get("/clientes/buscar")
def buscar_cliente(request: Request, nombre: str):
    clientes = DaoClientes().get_all(database)
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.nombre.lower() == nombre.lower():
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        return templates.TemplateResponse("cliente_encontrado.html", {"request": request, "cliente": cliente_encontrado})
    else:
        return templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes, "message": f"No se encontró el cliente '{nombre}'."})