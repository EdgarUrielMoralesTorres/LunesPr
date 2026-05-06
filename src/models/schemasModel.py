from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email: EmailStr
    contra: str= Field(min_length=8)
    apellido: str = Field(min_length=3, max_length=100)


class TareaSchems(BaseModel):
    titulo: str = Field(min_length=1,max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"    