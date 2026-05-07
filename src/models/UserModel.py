import bcrypt
from .database import Database


class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()

        hashed_pw = bcrypt.hashpw(usuario_data.contra.encode('utf-8'),salt)
        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            query = """INSERT INTO usuarios (nombre, apellido,telefono,email, contra,activo,fecha_regis,foto_perfil)VALUES (%s, %s, %s,%s, %s,%s,%s,%s)"""
            values = (usuario_data.nombre,usuario_data.apellido,usuario_data.telefono,usuario_data.email,hashed_pw.decode('utf-8'), usuario_data.activo,usuario_data.fecha_registro,usuario_data.foto_perfil)
            cursor.execute(query, values)
            conn.commit()

            return True, "Usuario registrado correctamente"

        except Exception as e:
            print("Error:", e)
            return False, str(e)

        finally:
            conn.close()

    def validar_login(self, email, contra):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            try:
                stored_hash = user['contra']

                if isinstance(stored_hash, str):
                    stored_hash = stored_hash.encode('utf-8')

                if bcrypt.checkpw(
                    contra.encode('utf-8'),
                    stored_hash
                ):
                    print("Login correcto")
                    return user

            except Exception as e:
                print(f"Error en validación: {e}")
                return None

        print("Login fallido")
        return None