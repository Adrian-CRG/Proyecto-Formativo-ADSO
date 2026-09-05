from flask import current_app
from Models.Proveedor import Proveedor
import uuid


class ProveedorService:

    def listar():
        sql = "SELECT * FROM T_PROVEEDOR"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        proveedores_l = []
        for p in data:
            proveedores_l.append(
                Proveedor(p[0], p[1], p[2], p[3]).to_dic()
            )
        return proveedores_l


    def crear(codigo, nombre):
        prov_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_PROVEEDOR
            (PROV_UUID, PROV_CODIGO, PROV_NOMBRE)
            VALUES (%s, %s, %s)
        """
        valores = (prov_uuid, codigo, nombre)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return Proveedor(new_id, prov_uuid, codigo, nombre).to_dic()


    def actualizar(id, codigo, nombre):
        sql = """
            UPDATE T_PROVEEDOR
            SET PROV_CODIGO = %s,
                PROV_NOMBRE = %s
            WHERE PROV_ID = %s
        """
        valores = (codigo, nombre, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_PROVEEDOR WHERE PROV_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def buscarPorCodigo(codigo):
        sql = "SELECT * FROM T_PROVEEDOR WHERE PROV_CODIGO = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (codigo,))
        data = c.fetchone()
        c.close()

        if data is None:
            return None

        return Proveedor(data[0], data[1], data[2], data[3]).to_dic()
