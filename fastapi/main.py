from typing import Union

from fastapi import FastAPI, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test", response_class=HTMLResponse)
async def test(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="index.html", context={"nombre": "pepe"}                                                      
    )

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    
    students = [ {"nombre": "pepe", "edad": 20,"score": 50}, {"nombre": "pepe", "edad": 20,"score": 50}, {"nombre": "pepe", "edad": 20,"score": 90}]
    return templates.TemplateResponse(
        request=request, name="students.html", context={"nombre": "pepe","students": students}                                                      
    )


