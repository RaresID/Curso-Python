from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para el modelo Pydantic y el endpoint POST
class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    disponible: Optional[bool] = True
    descripcion: Optional[str] = None
    

@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": f"Producto {producto.nombre} registrado con éxito con precio {producto.precio}€"
    }
    