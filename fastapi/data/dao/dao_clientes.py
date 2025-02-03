from data.modelo.cliente import Cliente
from fastapi import HTTPException

class DaoClientes:
    def get_all(self, db) -> list[Cliente]:
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM clientes")
        
        clientes_en_db = cursor.fetchall()
        
        clientes: list[Cliente] = list()
        
        for cliente in clientes_en_db:
            cliente = Cliente(id=cliente[0], nombre=cliente[1])
            clientes.append(cliente)
        
        cursor.close()
        return clientes


    def add(self, db, nombre: str):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM clientes WHERE nombre = %s", (nombre,))
        sql = ("INSERT INTO clientes (nombre) values (%s) ")
        data = (nombre,)
        cursor.execute(sql,data)
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

