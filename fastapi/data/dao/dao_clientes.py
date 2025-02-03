from data.modelo.cliente import Cliente
from fastapi import HTTPException

class DaoClientes:
    def get_all(self, db):
        cursor = db.cursor(dictionary=True)  # Devuelve un diccionario en vez de una tupla
        cursor.execute("SELECT id, nombre FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        return [Cliente(cliente["id"], cliente["nombre"]) for cliente in clientes]

    def add(self, db, cliente: Cliente):
        cursor = db.cursor()
        cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (cliente.nombre,))
        cliente.id = cursor.lastrowid  # Obtener el ID generado
        db.commit()
        cursor.close()
        return cliente

    def delete(self, db, nombre: str):
        cursor = db.cursor()
        cursor.execute("SELECT id FROM clientes WHERE nombre = %s", (nombre,))
        cliente = cursor.fetchone()

        if not cliente:
            return None  # Devuelve None si el cliente no existe
        
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente[0],))
        db.commit()
        cursor.close()
