from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/hola")
def hola(request: Request):
     apellido : str = "perez"
     return templates.TemplateResponse(
        request=request, name="hola.html" , 
        context={"nombre": "oscar","hhh": apellido}                   
    )


@app.get("/pllll")
def pompis(request: Request):
     nombre : str  = "oscar"
     apellido : str = "perez"

     return templates.TemplateResponse(
        request=request, name="pagina.html" , context={"nombre": nombre}                   
    )