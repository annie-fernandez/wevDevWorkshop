from pydantic import BaseModel

cur_id = 0

def increment():
    global cur_id
    cur_id += 1
    return cur_id

class Task(BaseModel):
    id: int
    description: str
    isComplete: bool

    def _init_(self, **data):
        super()._init_(id = increment(), **data)