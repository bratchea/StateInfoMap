import requests

from google.cloud import firestore
from scraper import StateScraper
from models.state import State


# initialize StateScraper

ss = StateScraper()


for state in ss.STATES:
    raw_state = ss.get_raw_state_info(state)
    clean_state = ss.clean_state_info(raw_state)
    state_obj = State(**clean_state)
    
    requests.post(url="http://127.0.0.1:8000/states/", json=state_obj.dict())