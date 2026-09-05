from flask import current_app
from Models.ProveedorInsumo import ProveedorInsumo
import uuid


class ProveedorInsumoService:

    def listar():
        sql = "SELECT * FROM T_PROVEEDOR_INSUMO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        prove_l = []
        for pi in data:
            prove_l.append(
                ProveedorInsumo(
                    pi[2], pi[3], pi[0], pi[1], pi[4], pi[5], pi[6], pi[7]
                ).to_dic()
            )
        return prove_l


    def crear(ins_id, prov_id, fecha, cantidad, precio, tipo_insumo):
        prove_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_PROVEEDOR_INSUMO
            (PROVE_INS_ID, PROVE_PROV_ID, PROVE_UUID, PROVE_FECHA,
             PROVE_CANTIDAD, PROVE_PRECIO, PROVE_TIPO_INSUMO)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (ins_id, prov_id, prove_uuid, fecha, cantidad, precio, tipo_insumo)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return ProveedorInsumo(
            new_id, prove_uuid, ins_id, prov_id, fecha, cantidad, precio, tipo_insumo
        ).to_dic()


    def actualizar(id, fecha, cantidad, precio, tipo_insumo):
        sql = """
            UPDATE T_PROVEEDOR_INSUMO
            SET PROVE_FECHA = %s,
                PROVE_CANTIDAD = %s,
                PROVE_PRECIO = %s,
                PROVE_TIPO_INSUMO = %s
            WHERE PROVE_ID = %s
        """
        valores = (fecha, cantidad, precio, tipo_insumo, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_PROVEEDOR_INSUMO WHERE PROVE_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorProveedor(prov_id):
        sql = "SELECT * FROM T_PROVEEDOR_INSUMO WHERE PROVE_PROV_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (prov_id,))
        data = c.fetchall()
        c.close()

        prove_l = []
        for pi in data:
            prove_l.append(
                ProveedorInsumo(
                    pi[2], pi[3], pi[0], pi[1], pi[4], pi[5], pi[6], pi[7]
                ).to_dic()
            )
        return prove_l


    def listarPorInsumo(ins_id):
        sql = "SELECT * FROM T_PROVEEDOR_INSUMO WHERE PROVE_INS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (ins_id,))
        data = c.fetchall()
        c.close()

        prove_l = []
        for pi in data:
            prove_l.append(
                ProveedorInsumo(
                    pi[2], pi[3], pi[0], pi[1], pi[4], pi[5], pi[6], pi[7]
                ).to_dic()
            )
        return prove_l
