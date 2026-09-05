from flask import current_app
from Models.ProductoInsumo import ProductoInsumo
import uuid


class ProductoInsumoService:

    def listar():
        sql = "SELECT * FROM T_PRODUCTO_INSUMO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        proins_l = []
        for pi in data:
            proins_l.append(
                ProductoInsumo(pi[0], pi[1], pi[2], pi[3], pi[4]).to_dic()
            )
        return proins_l


    def crear(pro_id, cantidad, fecha_fabricacion):
        proins_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_PRODUCTO_INSUMO
            (PROINS_UUID, PROINS_PRO_ID, PROINS_CANTIDAD, PROINS_FECHA_FABRICACION)
            VALUES (%s, %s, %s, %s)
        """
        valores = (proins_uuid, pro_id, cantidad, fecha_fabricacion)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return ProductoInsumo(
            new_id, proins_uuid, pro_id, cantidad, fecha_fabricacion
        ).to_dic()


    def actualizar(id, cantidad, fecha_fabricacion):
        sql = """
            UPDATE T_PRODUCTO_INSUMO
            SET PROINS_CANTIDAD = %s,
                PROINS_FECHA_FABRICACION = %s
            WHERE PROINS_ID = %s
        """
        valores = (cantidad, fecha_fabricacion, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_PRODUCTO_INSUMO WHERE PROINS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorProducto(pro_id):
        sql = "SELECT * FROM T_PRODUCTO_INSUMO WHERE PROINS_PRO_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (pro_id,))
        data = c.fetchall()
        c.close()

        proins_l = []
        for pi in data:
            proins_l.append(
                ProductoInsumo(pi[0], pi[1], pi[2], pi[3], pi[4]).to_dic()
            )
        return proins_l
