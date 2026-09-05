class Proveedor:
    def __init__(self, id, uuid, codigo, nombre):
        self.PROV_ID      = id
        self.PROV_UUID    = uuid
        self.PROV_CODIGO  = codigo
        self.PROV_NOMBRE  = nombre

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Proveedor"""
        return {
            "id"      : self.PROV_ID,
            "uuid"    : self.PROV_UUID,
            "codigo"  : self.PROV_CODIGO,
            "nombre"  : self.PROV_NOMBRE
        }
