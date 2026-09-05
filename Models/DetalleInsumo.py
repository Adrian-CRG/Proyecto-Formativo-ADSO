class DetalleInsumo:
    def __init__(self, id, uuid, cantidad_disp, proins_id, ins_id):
        self.DETINS_ID             = id
        self.DETINS_UUID           = uuid
        self.DETINS_CANTIDAD_DISP  = cantidad_disp
        self.DETINS_PROINS_ID      = proins_id
        self.DETINS_INS_ID         = ins_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase DetalleInsumo"""
        return {
            "id"             : self.DETINS_ID,
            "uuid"           : self.DETINS_UUID,
            "cantidad_disp"  : self.DETINS_CANTIDAD_DISP,
            "proins_id"      : self.DETINS_PROINS_ID,
            "ins_id"         : self.DETINS_INS_ID
        }
