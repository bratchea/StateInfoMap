from fastapi import FastAPI
from models.state import State


app = FastAPI()

@app.get("/states/{state}")
def get_state_info(state):
    return {"message": f"State Info Requested: {state}"}


@app.post("/states/{state}")
def add_state_info(state):
    return {"message": f"Added {state}"}
