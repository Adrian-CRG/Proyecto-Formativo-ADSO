from flask import Blueprint
from Controllers.DetalleInsumoController import DetalleInsumoController


detins_bp = Blueprint('detalle_insumo_bp', __name__)


# Listar todos los detalles de insumo
@detins_bp.route('/', methods=['GET'])
def listarDetallesInsumo():
    return DetalleInsumoController.listar()


# Crear un detalle de insumo
@detins_bp.route('/', methods=['POST'])
def crearDetalleInsumo():
    return DetalleInsumoController.crear()


# Actualizar un detalle de insumo
@detins_bp.route('/', methods=['PUT'])
def actualizarDetalleInsumo():
    return DetalleInsumoController.actualizar()


# Eliminar un detalle de insumo
@detins_bp.route('/<int:id>', methods=['DELETE'])
def eliminarDetalleInsumo(id):
    return DetalleInsumoController.eliminar(id)


# Listar por producto insumo
@detins_bp.route('/producto-insumo/<int:proins_id>', methods=['GET'])
def listarPorProductoInsumo(proins_id):
    return DetalleInsumoController.listarPorProductoInsumo(proins_id)


# Listar por insumo
@detins_bp.route('/insumo/<int:ins_id>', methods=['GET'])
def listarPorInsumo(ins_id):
    return DetalleInsumoController.listarPorInsumo(ins_id)
