from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="Users API",
    description="Foydalanuvchilar ma'lumotlari",
    version="1.0.0"
)

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    city: str
    phone: str
    website: Optional[str] = None

users = [
    User(
        id=1,
        name="Ali Valiyev",
        username="aliv",
        email="ali@mail.com",
        city="Toshkent",
        phone="+998901234567",
        website="ali.uz"
    ),
    User(
        id=2,
        name="Zarina Karimova",
        username="zarina",
        email="zarina@mail.com",
        city="Samarqand",
        phone="+998912345678",
        website="zarina.uz"
    ),
    User(
        id=3,
        name="Bobur Abdullayev",
        username="bobur",
        email="bobur@mail.com",
        city="Buxoro",
        phone="+998933456789",
        website=None
    ),
    User(
        id=4,
        name="Dilnoza Rahimova",
        username="dilnoza",
        email="dilnoza@mail.com",
        city="Namangan",
        phone="+998944567890",
        website="dilnoza.uz"
    ),
    User(
        id=5,
        name="Jasur Tursunov",
        username="jasur",
        email="jasur@mail.com",
        city="Farg'ona",
        phone="+998955678901",
        website="jasur.uz"
    )
]

@app.get("/")
def home():
    return {
        "message": "Users API ishga tushdi",
        "endpoints": {
            "all_users": "/users",
            "user_by_id": "/users/{id}",
            "user_by_city": "/users/city/{city}",
            "docs": "/docs"
        }
    }

@app.get("/users", response_model=List[User])
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"User ID {user_id} topilmadi")

@app.get("/users/city/{city_name}")
def get_user_by_city(city_name: str):
    for user in users:
        if user.city.lower() == city_name.lower():
            return user
    raise HTTPException(status_code=404, detail=f"{city_name} shahrida user topilmadi")

@app.get("/users/username/{username}")
def get_user_by_username(username: str):
    for user in users:
        if user.username.lower() == username.lower():
            return user
    raise HTTPException(status_code=404, detail=f"{username} topilmadi")

@app.get("/cities")
def get_cities():
    cities = list(set(user.city for user in users))
    return {"cities": cities, "count": len(cities)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)