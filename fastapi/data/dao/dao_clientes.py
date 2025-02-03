from data.modelo.cliente import Cliente
from fastapi import HTTPException

class DaoClientes:
    def get_all(self, db) -> list[Cliente]:
        cursor = db.cursor()
        
        cursor.execute("SELECT id, nombre FROM clientes")
        
        clientes_en_db = cursor.fetchall()
        
        clientes: list[Cliente] = []
        
        for cliente in clientes_en_db:
            cliente_obj = Cliente(cliente[0], cliente[1])
            clientes.append(cliente_obj)
        
        cursor.close()
        return clientes

    def add(self, db, cliente: Cliente):
        cursor = db.cursor()
        if cliente.nombre:
            cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (cliente.nombre,))
        db.commit()
        cursor.close()

    def delete(self, db, nombre: str):
        cursor = db.cursor()
    
    
        cursor.execute("SELECT * FROM clientes WHERE nombre = %s", (nombre,))
        cliente = cursor.fetchone()
    
        if not cliente:
            raise HTTPException(status_code=404, detail=f"No se encontró el cliente con nombre '{nombre}'")
    
   
        cursor.execute("DELETE FROM clientes WHERE nombre = %s", (nombre,))
        db.commit()
        cursor.close()