from pydantic import BaseModel

class Authentication(BaseModel):
    account_caller: str
    private_key: str