from flask import current_app
from Models.DetalleCompra import DetalleCompra
import uuid


class DetalleCompraService:

    def listar():
        sql = "SELECT * FROM T_DETALLE_COMPRA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        detcom_l = []
        for dc in data:
            detcom_l.append(
                DetalleCompra(
                    dc[2], dc[3], dc[0], dc[1], dc[4], dc[5], dc[6], dc[7]
                ).to_dic()
            )
        return detcom_l


    def crear(comp_id, pro_id, cantidad, precio, fecha, factura):
        detcom_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_DETALLE_COMPRA
            (DETCOM_COMP_ID, DETCOM_PRO_ID, DETCOM_UUID, DETCOM_CANTIDAD,
             DETCOM_PRECIO, DETCOM_FECHA, DETCOM_FACTURA)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (comp_id, pro_id, detcom_uuid, cantidad, precio, fecha, factura)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return DetalleCompra(
            new_id, detcom_uuid, comp_id, pro_id, cantidad, precio, fecha, factura
        ).to_dic()


    def actualizar(id, cantidad, precio, fecha, factura):
        sql = """
            UPDATE T_DETALLE_COMPRA
            SET DETCOM_CANTIDAD = %s,
                DETCOM_PRECIO = %s,
                DETCOM_FECHA = %s,
                DETCOM_FACTURA = %s
            WHERE DETCOM_ID = %s
        """
        valores = (cantidad, precio, fecha, factura, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_DETALLE_COMPRA WHERE DETCOM_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorCompra(comp_id):
        sql = "SELECT * FROM T_DETALLE_COMPRA WHERE DETCOM_COMP_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (comp_id,))
        data = c.fetchall()
        c.close()

        detcom_l = []
        for dc in data:
            detcom_l.append(
                DetalleCompra(
                    dc[2], dc[3], dc[0], dc[1], dc[4], dc[5], dc[6], dc[7]
                ).to_dic()
            )
        return detcom_l


    def buscarPorFactura(factura):
        sql = "SELECT * FROM T_DETALLE_COMPRA WHERE DETCOM_FACTURA = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (factura,))
        data = c.fetchone()
        c.close()

        if data is None:
            return None

        return DetalleCompra(
            data[2], data[3], data[0], data[1], data[4], data[5], data[6], data[7]
        ).to_dic()
