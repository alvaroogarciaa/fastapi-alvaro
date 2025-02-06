from data.modelo.cliente import Cliente
from fastapi import HTTPException

class DaoClientes:
    def get_all(self, db) -> list[Cliente]:
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT id, nombre FROM clientes")
    
        clientes_en_db = cursor.fetchall()
        clientes = [Cliente(id, nombre) for id, nombre in clientes_en_db]
    
        cursor.close()
        return clientes




    def add(self, db, cliente: Cliente):
        cursor = db.cursor()
        cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (cliente.nombre,))
    
        db.commit()
        cursor.nextset()
        cursor.close()



    def delete(self, db, id: int):
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
    
        if not cliente:
            raise HTTPException(status_code=404, detail=f"No se encontró el cliente con ID '{id}'")
    
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        db.commit()
        cursor.close()


