class CategoriaProducto:
    def __init__(self, id, uuid, pro_id, cat_id):
        self.CATPRO_ID      = id
        self.CATPRO_UUID    = uuid
        self.CATPRO_PRO_ID  = pro_id
        self.CATPRO_CAT_ID  = cat_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase CategoriaProducto"""
        return {
            "id"      : self.CATPRO_ID,
            "uuid"    : self.CATPRO_UUID,
            "pro_id"  : self.CATPRO_PRO_ID,
            "cat_id"  : self.CATPRO_CAT_ID
        }
