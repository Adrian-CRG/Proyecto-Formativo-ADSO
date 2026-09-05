class DetalleCompra:
    def __init__(self, id, uuid, comp_id, pro_id, cantidad, precio, fecha, factura):
        self.DETCOM_ID       = id
        self.DETCOM_UUID     = uuid
        self.DETCOM_COMP_ID  = comp_id
        self.DETCOM_PRO_ID   = pro_id
        self.DETCOM_CANTIDAD = cantidad
        self.DETCOM_PRECIO   = precio
        self.DETCOM_FECHA    = fecha
        self.DETCOM_FACTURA  = factura

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase DetalleCompra"""
        return {
            "id"       : self.DETCOM_ID,
            "uuid"     : self.DETCOM_UUID,
            "comp_id"  : self.DETCOM_COMP_ID,
            "pro_id"   : self.DETCOM_PRO_ID,
            "cantidad" : self.DETCOM_CANTIDAD,
            "precio"   : self.DETCOM_PRECIO,
            "fecha"    : self.DETCOM_FECHA,
            "factura"  : self.DETCOM_FACTURA
        }
