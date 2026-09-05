from flask import current_app
from Models.DetalleInsumo import DetalleInsumo
import uuid


class DetalleInsumoService:

    def listar():
        sql = "SELECT * FROM T_DETALLE_INSUMO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        detins_l = []
        for di in data:
            detins_l.append(
                DetalleInsumo(di[0], di[1], di[2], di[3], di[4]).to_dic()
            )
        return detins_l


    def crear(cantidad_disp, proins_id, ins_id):
        detins_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_DETALLE_INSUMO
            (DETINS_UUID, DETINS_CANTIDAD_DISP, DETINS_PROINS_ID, DETINS_INS_ID)
            VALUES (%s, %s, %s, %s)
        """
        valores = (detins_uuid, cantidad_disp, proins_id, ins_id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return DetalleInsumo(
            new_id, detins_uuid, cantidad_disp, proins_id, ins_id
        ).to_dic()


    def actualizar(id, cantidad_disp):
        sql = """
            UPDATE T_DETALLE_INSUMO
            SET DETINS_CANTIDAD_DISP = %s
            WHERE DETINS_ID = %s
        """
        valores = (cantidad_disp, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_DETALLE_INSUMO WHERE DETINS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorProductoInsumo(proins_id):
        sql = "SELECT * FROM T_DETALLE_INSUMO WHERE DETINS_PROINS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (proins_id,))
        data = c.fetchall()
        c.close()

        detins_l = []
        for di in data:
            detins_l.append(
                DetalleInsumo(di[0], di[1], di[2], di[3], di[4]).to_dic()
            )
        return detins_l


    def listarPorInsumo(ins_id):
        sql = "SELECT * FROM T_DETALLE_INSUMO WHERE DETINS_INS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (ins_id,))
        data = c.fetchall()
        c.close()

        detins_l = []
        for di in data:
            detins_l.append(
                DetalleInsumo(di[0], di[1], di[2], di[3], di[4]).to_dic()
            )
        return detins_l
