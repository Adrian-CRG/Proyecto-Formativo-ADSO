from flask import Blueprint
from Controllers.ProductoInsumoController import ProductoInsumoController


proins_bp = Blueprint('producto_insumo_bp', __name__)


# Listar todos los productos insumos
@proins_bp.route('/', methods=['GET'])
def listarProductosInsumos():
    return ProductoInsumoController.listar()


# Crear un producto insumo
@proins_bp.route('/', methods=['POST'])
def crearProductoInsumo():
    return ProductoInsumoController.crear()


# Actualizar un producto insumo
@proins_bp.route('/', methods=['PUT'])
def actualizarProductoInsumo():
    return ProductoInsumoController.actualizar()


# Eliminar un producto insumo
@proins_bp.route('/<int:id>', methods=['DELETE'])
def eliminarProductoInsumo(id):
    return ProductoInsumoController.eliminar(id)


# Listar por producto
@proins_bp.route('/producto/<int:pro_id>', methods=['GET'])
def listarPorProducto(pro_id):
    return ProductoInsumoController.listarPorProducto(pro_id)
