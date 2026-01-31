from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class GastoUpdate(BaseModel):
    monto: Optional[float] = Field(gt=0)
    categoria: Optional[str]
    descripcion: Optional[str]
    fecha: Optional[date]

class GastoOut(BaseModel):
    id: int
    monto: float
    categoria: str
    descripcion: Optional[str]
    fecha: date

    class Config:
        from_attributes = True

class GastoUpdate(BaseModel):
    monto: Optional[float] = Field(gt=0)
    categoria: Optional[str]
    descripcion: Optional[str]
    fecha: Optional[date]

class GastoOut(BaseModel):
    id: int
    monto: float
    categoria: str
    descripcion: Optional[str]
    fecha: date

    class Config:
        from_attributes = True