from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, include_email:bool = False, format: str = "basic"):
    user_data = {
        "user_id":user_id,
        "name": f"Usuario {user_id}",
        "format": format
    }
    
    #  añadir email si include_email es True
    
    if include_email:
        user_data["email"] = f"user{user_id}@example.com"
        
    return user_data
