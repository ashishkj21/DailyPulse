from pydantic import BaseModel

class Commit(BaseModel):
    sha: str
    message: str
    author: str
