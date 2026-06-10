from typing import Optional

from pydantic import BaseModel


class CreateCustomer(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    
class ResponseCustomer(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True