from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class GastoCreate(BaseModel):
    monto: float = Field(gt=0)
    categoria: str = Field(min_length=1, max_length=50)
    descripcion: Optional[str] = Field(default=None, max_length=200)
    fecha: date

class GastoOut(BaseModel):
    id: int
    monto: float
    categoria: str
    descripcion: Optional[str]
    fecha: date

    class Config:
        from_attributes = True
