# Aqui se iniciará la api
from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from datetime import datetime

lista =[]
#Crear boton
@app.post("/Botones")
def Crear_Boton(nombre: str, color: str):
    for elemento in lista:
        if nombre == elemento['nombre']:
            raise HTTPException(status_code=400, detail="Elija otro nombre, ese ya existe")
    
    id = len(lista)
    boton = {
        "id": id,
        "nombre": nombre,
        "estado": False,
        "color": color,
        "fecha": datetime.now()
    }
    
    lista.append(boton)
    return {"mensaje": "Botón creado correctamente", "boton": boton}

@app.get("/Botones/{nombre}")
def Leer_boton(nombre):
    for elemento in lista:
        if nombre in elemento.values():
            datos = elemento.values()
            print(datos)
            return elemento
            break
        else:
            pass
Leer_boton("boton2")
@app.put("/Botones/{nombre}")
def Modificar_Boton(nombre: str, campo: str, nuevo_valor: Union[str, bool]):
    for elemento in lista:
        if nombre == elemento['nombre']:
            if campo in elemento:
                elemento[campo] = nuevo_valor  
                return {"mensaje": f"Botón '{nombre}' actualizado correctamente", "boton": elemento}
            else:
                raise HTTPException(status_code=400, detail=f"Campo '{campo}' no válido para modificar")
    
    raise HTTPException(status_code=404, detail=f"Botón '{nombre}' no encontrado")