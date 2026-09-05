class ProductoInsumo:
    def __init__(self, id, uuid, pro_id, cantidad, fecha_fabricacion):
        self.PROINS_ID                = id
        self.PROINS_UUID              = uuid
        self.PROINS_PRO_ID            = pro_id
        self.PROINS_CANTIDAD          = cantidad
        self.PROINS_FECHA_FABRICACION = fecha_fabricacion

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase ProductoInsumo"""
        return {
            "id"                : self.PROINS_ID,
            "uuid"              : self.PROINS_UUID,
            "pro_id"            : self.PROINS_PRO_ID,
            "cantidad"          : self.PROINS_CANTIDAD,
            "fecha_fabricacion" : self.PROINS_FECHA_FABRICACION
        }
