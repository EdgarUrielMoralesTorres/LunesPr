from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, contra):     
        try:
            user = self.model.validar_login(email, contra)

            if user:
                return user, "Login correcto"
            else:
                return None, "Correo o contraseña incorrectos"

        except Exception as e:
            return None, str(e)
    def register(self, nombre, apellido, telefono,email, contra):
        print(contra)
        try:
            usuario_data = UsuarioSchema(nombre=nombre,telefono=telefono,email=email,contra=contra, apellido=apellido,)
            success, msg = self.model.registrar(usuario_data)
            return success, msg

        except ValidationError as e:
            print(e)
            return False, e.errors()[0]['msg']

        except Exception as e:
            return False, str(e)