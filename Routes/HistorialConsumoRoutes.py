from flask import Blueprint
from Controllers.HistorialConsumoController import HistorialConsumoController


hiscon_bp = Blueprint('historial_consumo_bp', __name__)


# Listar todos los historiales de consumo
@hiscon_bp.route('/', methods=['GET'])
def listarHistorialesConsumo():
    return HistorialConsumoController.listar()


# Crear un historial de consumo
@hiscon_bp.route('/', methods=['POST'])
def crearHistorialConsumo():
    return HistorialConsumoController.crear()


# Actualizar un historial de consumo
@hiscon_bp.route('/', methods=['PUT'])
def actualizarHistorialConsumo():
    return HistorialConsumoController.actualizar()


# Eliminar un historial de consumo
@hiscon_bp.route('/<int:id>', methods=['DELETE'])
def eliminarHistorialConsumo(id):
    return HistorialConsumoController.eliminar(id)


# Listar por proveedor insumo
@hiscon_bp.route('/proveedor-insumo/<int:prove_id>', methods=['GET'])
def listarPorProveedorInsumo(prove_id):
    return HistorialConsumoController.listarPorProveedorInsumo(prove_id)


# Listar por detalle insumo
@hiscon_bp.route('/detalle-insumo/<int:detins_id>', methods=['GET'])
def listarPorDetalleInsumo(detins_id):
    return HistorialConsumoController.listarPorDetalleInsumo(detins_id)
