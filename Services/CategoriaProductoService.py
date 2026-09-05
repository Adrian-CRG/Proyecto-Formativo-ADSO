from flask import current_app
from Models.CategoriaProducto import CategoriaProducto
import uuid


class CategoriaProductoService:

    def listar():
        sql = "SELECT * FROM T_CATEGORIA_PRODUCTO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        catpro_l = []
        for cp in data:
            catpro_l.append(
                CategoriaProducto(cp[0], cp[1], cp[2], cp[3]).to_dic()
            )
        return catpro_l


    def crear(pro_id, cat_id):
        catpro_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_CATEGORIA_PRODUCTO
            (CATPRO_UUID, CATPRO_PRO_ID, CATPRO_CAT_ID)
            VALUES (%s, %s, %s)
        """
        valores = (catpro_uuid, pro_id, cat_id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return CategoriaProducto(new_id, catpro_uuid, pro_id, cat_id).to_dic()


    def eliminar(id):
        sql = "DELETE FROM T_CATEGORIA_PRODUCTO WHERE CATPRO_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def listarPorProducto(pro_id):
        sql = "SELECT * FROM T_CATEGORIA_PRODUCTO WHERE CATPRO_PRO_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (pro_id,))
        data = c.fetchall()
        c.close()

        catpro_l = []
        for cp in data:
            catpro_l.append(
                CategoriaProducto(cp[0], cp[1], cp[2], cp[3]).to_dic()
            )
        return catpro_l


    def listarPorCategoria(cat_id):
        sql = "SELECT * FROM T_CATEGORIA_PRODUCTO WHERE CATPRO_CAT_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (cat_id,))
        data = c.fetchall()
        c.close()

        catpro_l = []
        for cp in data:
            catpro_l.append(
                CategoriaProducto(cp[0], cp[1], cp[2], cp[3]).to_dic()
            )
        return catpro_l
