from pydantic import BaseModel, Extra


class State(BaseModel, extra=Extra.ignore):
    """
    model of a state with given attributes
    """
    name: str
    capital: str
    largest_city: str
    governor: str
    admitted: str
    area: str
