from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int
    activo: bool
    
# modelo con campos opcionales y valores por defecto
class Producto(BaseModel):
    nombre: str
    precio: float
    descipcion: Optional[str] = None
    disponible: bool = True