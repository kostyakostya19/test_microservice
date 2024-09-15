from fastapi import FastAPI
from get_data import get_data_from_rabbitmq

app = FastAPI()

@app.get("/data")
async def get_data():
    data = get_data_from_rabbitmq()
    if data:
        return {"data": data.decode("utf-8")}
    return {"message": "No data in the queue"}