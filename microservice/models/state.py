from pydantic import BaseModel, Extra


class State(BaseModel, extra=Extra.allow):
    capital: str
    largest_city: str
    governor: str
    admitted: str
    area: str
