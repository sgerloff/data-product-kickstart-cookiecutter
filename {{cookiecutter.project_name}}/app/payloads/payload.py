from pydantic import BaseModel


class Payload(BaseModel):
    someInput: str
