from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Створюємо застосунок для роботи з тренуваннями
app = FastAPI(title="Training Service")

# Список для зберігання тренувань
trainings = []

# Модель даних одного тренування
class Training(BaseModel):
    client: str
    date: str
    time: str

# 1. Додавання тренування
@app.post("/trainings")
def add_training(training: Training):
    trainings.append(training)
    return {"message": "Training added successfully!"}

# 2. Перегляд усіх тренувань
@app.get("/trainings")
def list_trainings():
    if len(trainings) == 0:
        return {"message": "No trainings available."}

    return [
        {
            "number": i + 1,
            "client": training.client,
            "date": training.date,
            "time": training.time
        }
        for i, training in enumerate(trainings)
    ]

# 3. Видалення тренування за номером
@app.delete("/trainings/{number}")
def delete_training(number: int):
    if len(trainings) == 0:
        raise HTTPException(
            status_code=404,
            detail="No trainings available to delete."
        )

    if number < 1 or number > len(trainings):
        raise HTTPException(
            status_code=404,
            detail="Invalid training number. Please try again."
        )

    del trainings[number - 1]
    return {"message": "Training deleted successfully!"}


# 4. Пошук тренувань за ім'ям клієнта
@app.get("/trainings/client/{client_name}")
def find_client_trainings(client_name: str):
    result = [
        {
            "client": training.client,
            "date": training.date,
            "time": training.time
        }
        for training in trainings
        if training.client.lower() == client_name.lower()
    ]

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Client not found."
        )

    return result