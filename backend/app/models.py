from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Gastos(Base):
    __tablename__ = 'gastos'

    id = Column(Integer, primary_key=True, index=True)
    precio = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    fecha = Column(Date, nullable=False)