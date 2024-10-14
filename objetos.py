"objeto Boton"
from typing import Union
from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

class Boton:
    id_previa = 1
    lista_de_botones = []

    def __init__(self, nombre, color):
        
        self.nombre = nombre
        self.color = color
        self.estado = False
        Boton.id_previa +=  1
        self.fecha = datetime.now()

        Boton.lista_de_botones.append(self)


@app.post("/Botones")
def crear_boton(nombre: str, color: str):
    for elemento in Boton.lista_de_botones:
        if nombre == elemento.nombre:
            raise HTTPException(status_code=400, detail="Elija otro nombre, ese ya existe")
        nuevo_boton = Boton(nombre, color)
    return {"mensaje": "Botón creado correctamente", "nombre": nuevo_boton.nombre}
    

@app.get("/Botones/{nombre}")
def leer_boton(nombre: str): 
    for boton in Boton.lista_de_botones:
        if boton.nombre == nombre:
            
            return {
                "id": boton.id,
                "nombre": boton.nombre,
                "color": boton.color,
                "estado": boton.estado,
                "fecha": boton.fecha
            }
    
    raise HTTPException(status_code=404, detail="Botón no encontrado")


@app.put("/Botones/{nombre}")
def modificar_boton(nombre: str, campo: str, nuevo_valor: Union[str, bool]):
    for boton in Boton.lista_de_botones:
        if boton.nombre == nombre:
            if campo in boton:
                boton.campo = nuevo_valor  
                return {"mensaje": f"Botón '{nombre}' actualizado correctamente", "boton":boton}
            else:
                raise HTTPException(status_code=400, detail=f"Campo '{campo}' no válido para modificar")
    
    raise HTTPException(status_code=404, detail=f"Botón '{nombre}' no encontrado")

@app.delate("/Botones/{nombre}")
def borrar_boton(nombre: str):
    for index, boton in enumerate(Boton.lista_de_botones):
        if boton.nombre == nombre:
            del Boton.lista_de_botones[index]
            return {"mensaje": f"Botón '{nombre}' eliminado correctamente"}
    
    raise HTTPException(status_code=404, detail="Botón no encontrado")