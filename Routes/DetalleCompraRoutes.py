from flask import Blueprint
from Controllers.DetalleCompraController import DetalleCompraController


detcom_bp = Blueprint('detalle_compra_bp', __name__)


# Listar todos los detalles de compra
@detcom_bp.route('/', methods=['GET'])
def listarDetallesCompra():
    return DetalleCompraController.listar()


# Crear un detalle de compra
@detcom_bp.route('/', methods=['POST'])
def crearDetalleCompra():
    return DetalleCompraController.crear()


# Actualizar un detalle de compra
@detcom_bp.route('/', methods=['PUT'])
def actualizarDetalleCompra():
    return DetalleCompraController.actualizar()


# Eliminar un detalle de compra
@detcom_bp.route('/<int:id>', methods=['DELETE'])
def eliminarDetalleCompra(id):
    return DetalleCompraController.eliminar(id)


# Listar por compra
@detcom_bp.route('/compra/<int:comp_id>', methods=['GET'])
def listarPorCompra(comp_id):
    return DetalleCompraController.listarPorCompra(comp_id)


# Buscar por factura
@detcom_bp.route('/factura/<factura>', methods=['GET'])
def buscarPorFactura(factura):
    return DetalleCompraController.buscarPorFactura(factura)
