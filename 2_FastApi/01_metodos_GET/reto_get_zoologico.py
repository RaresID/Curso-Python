from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()


# Escribe aquí tu código para los endpoints GET
@app.get("/animales")
def obtener_animales():
    return {"animales": ["Leon", "Perro", "Jirafa","Cebra"]}

@app.get("/zoologico")
def obtener_zoologico():
    return {
        "nombre": "ZooPark",
        "cantidad_animales": 32,
        "Apertura": True,
        "Horario_atencion":"9:00-17:00"
    } 
    
@app.get("/estadisticas")
def obtener_estadisticas():
    return {
        "general": {
            "nombre": "ZooPark",
            "ubicacion": "Zaragoza"
        },
        "datos": {
            "total_especies":32,
            "animales_populares":"Rinoceronte"
        },
        "Estado_operacional":{
            "Apertura":True,
            "Empleados_presentes":2
        }
        }
