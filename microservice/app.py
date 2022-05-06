from fastapi import FastAPI, HTTPException
from google.cloud import firestore
from typing import Dict, Any
from models.state import State


app = FastAPI()

@app.get("/states/{state}")
def get_state_info(state: str):
    """
    Returns a state if it exists in firestore db
    """
    client = firestore.Client()

    state_ref = client.collection("states").document(state)
    state_doc = state_ref.get()

    if not state_doc.exists:
        raise HTTPException(status_code=404, detail=f"The State {state} Not Found")
    return state


@app.get("/states")
def all_states():
    """
    Returns all states in firestore db
    """
    return {"message": "Not Implemented"}


@app.post("/states", status_code=201)
async def add_state_info(state: State):
    """
    Add a state to the firestore db
    """
    return state
