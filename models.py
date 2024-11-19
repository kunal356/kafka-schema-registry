from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    title: str