from .database import Database

class TareaModel:
    def __init__(self):
        self.db=Database()
    
    def listar_por_usuario(self, idUs):
     conn = self.db.get_connection()    
     cursor = conn.cursor(dictionary=True)
     query = "SELECT * FROM tareas WHERE idUs = %s ORDER BY fecha_limit ASC"
     cursor.execute(query,(idUs,))
     resultado =cursor.fetchall()
     conn.close()
     return resultado

    def crear(self,idUs,titulo,descripcion,prioridad, clasificacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query ="""INSERT INTO tareas (idUs, titulo, descripcion, prioridad, clasificacion)
                VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(query,(idUs,titulo,descripcion,prioridad,clasificacion))
        conn.commit()
        conn.close()        