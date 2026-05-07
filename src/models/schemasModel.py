from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email: EmailStr
    contra: str= Field(min_length=8)
    apellido: str = Field(min_length=3, max_length=100)
    telefono: Optional[str] = Field(None, min_length=10, max_length=15)
    
    activo: bool = True
    fecha_registro: datetime = Field(default_factory=datetime.now)
    ultimo_ingreso: datetime = Field(default_factory=datetime.now)
    foto_perfil: Optional[str] = None


class TareaSchems(BaseModel):
    titulo: str = Field(min_length=1,max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"    
    
    