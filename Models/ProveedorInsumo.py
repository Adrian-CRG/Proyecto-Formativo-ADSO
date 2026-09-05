class ProveedorInsumo:
    def __init__(self, id, uuid, ins_id, prov_id, fecha, cantidad, precio, tipo_insumo):
        self.PROVE_ID           = id
        self.PROVE_UUID         = uuid
        self.PROVE_INS_ID       = ins_id
        self.PROVE_PROV_ID      = prov_id
        self.PROVE_FECHA        = fecha
        self.PROVE_CANTIDAD     = cantidad
        self.PROVE_PRECIO       = precio
        self.PROVE_TIPO_INSUMO  = tipo_insumo

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase ProveedorInsumo"""
        return {
            "id"           : self.PROVE_ID,
            "uuid"         : self.PROVE_UUID,
            "ins_id"       : self.PROVE_INS_ID,
            "prov_id"      : self.PROVE_PROV_ID,
            "fecha"        : self.PROVE_FECHA,
            "cantidad"     : self.PROVE_CANTIDAD,
            "precio"       : self.PROVE_PRECIO,
            "tipo_insumo"  : self.PROVE_TIPO_INSUMO
        }
