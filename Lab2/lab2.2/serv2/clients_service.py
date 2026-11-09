
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Clients Service")

# Список для зберігання клієнтів
clients = []


# Модель даних клієнта
class Client(BaseModel):
    name: str


# 1. Додавання клієнта
@app.post("/clients")
def add_client(client: Client):
    for existing_client in clients:
        if existing_client["name"].lower() == client.name.lower():
            raise HTTPException(
                status_code=400,
                detail="Client already exists."
            )

    clients.append({"name": client.name})
    return {"message": "Client added successfully!"}


# 2. Перегляд усіх клієнтів
@app.get("/clients")
def list_clients():
    if len(clients) == 0:
        return {"message": "No clients available."}

    return clients


# 3. Пошук клієнта за ім'ям
@app.get("/clients/{client_name}")
def find_client(client_name: str):
    for client in clients:
        if client["name"].lower() == client_name.lower():
            return client

    raise HTTPException(
        status_code=404,
        detail="Client not found."
    )
