class HistorialConsumo:
    def __init__(self, id, uuid, consumo, disponibilidad, prove_id, detins_id):
        self.HISCON_ID              = id
        self.HISCON_UUID            = uuid
        self.HISCON_CONSUMO         = consumo
        self.HISCON_DISPONIBILIDAD  = disponibilidad
        self.HISCON_PROVE_ID        = prove_id
        self.HISCON_DETINS_ID       = detins_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase HistorialConsumo"""
        return {
            "id"              : self.HISCON_ID,
            "uuid"            : self.HISCON_UUID,
            "consumo"         : self.HISCON_CONSUMO,
            "disponibilidad"  : self.HISCON_DISPONIBILIDAD,
            "prove_id"        : self.HISCON_PROVE_ID,
            "detins_id"       : self.HISCON_DETINS_ID
        }
