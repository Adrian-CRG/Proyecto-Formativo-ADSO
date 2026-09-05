from flask import current_app
from Models.HistorialConsumo import HistorialConsumo
import uuid


class HistorialConsumoService:

    def listar():
        sql = "SELECT * FROM T_HISTORIAL_CONSUMO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        hiscon_l = []
        for hc in data:
            hiscon_l.append(
                HistorialConsumo(hc[0], hc[1], hc[2], hc[3], hc[4], hc[5]).to_dic()
            )
        return hiscon_l


    def crear(consumo, disponibilidad, prove_id, detins_id):
        hiscon_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_HISTORIAL_CONSUMO
            (HISCON_UUID, HISCON_CONSUMO, HISCON_DISPONIBILIDAD,
             HISCON_PROVE_ID, HISCON_DETINS_ID)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (hiscon_uuid, consumo, disponibilidad, prove_id, detins_id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return HistorialConsumo(
            new_id, hiscon_uuid, consumo, disponibilidad, prove_id, detins_id
        ).to_dic()


    def actualizar(id, consumo, disponibilidad):
        sql = """
            UPDATE T_HISTORIAL_CONSUMO
            SET HISCON_CONSUMO = %s,
                HISCON_DISPONIBILIDAD = %s
            WHERE HISCON_ID = %s
        """
        valores = (consumo, disponibilidad, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_HISTORIAL_CONSUMO WHERE HISCON_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorProveedorInsumo(prove_id):
        sql = "SELECT * FROM T_HISTORIAL_CONSUMO WHERE HISCON_PROVE_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (prove_id,))
        data = c.fetchall()
        c.close()

        hiscon_l = []
        for hc in data:
            hiscon_l.append(
                HistorialConsumo(hc[0], hc[1], hc[2], hc[3], hc[4], hc[5]).to_dic()
            )
        return hiscon_l


    def listarPorDetalleInsumo(detins_id):
        sql = "SELECT * FROM T_HISTORIAL_CONSUMO WHERE HISCON_DETINS_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (detins_id,))
        data = c.fetchall()
        c.close()

        hiscon_l = []
        for hc in data:
            hiscon_l.append(
                HistorialConsumo(hc[0], hc[1], hc[2], hc[3], hc[4], hc[5]).to_dic()
            )
        return hiscon_l
