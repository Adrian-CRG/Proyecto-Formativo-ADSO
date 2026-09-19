from flask import Blueprint
from Controllers.ProductoController import ProductoController

pro_bp = Blueprint("producto_bp", __name__, url_prefix="/productos")


# Listar todos los productos
@pro_bp.route('/', methods=['GET'])
def listarProductos():
    return ProductoController.listar()


# Crear un producto
@pro_bp.route('/', methods=['POST'])
def crearProducto():
    return ProductoController.crear()


# Actualizar un producto
@pro_bp.route('/', methods=['PUT'])
def actualizarProducto():
    return ProductoController.actualizar()


# Eliminar un producto
@pro_bp.route('/<int:id>', methods=['DELETE'])
def eliminarProducto(id):
    return ProductoController.eliminar(id)


# Buscar producto por código
@pro_bp.route('/codigo/<codigo>', methods=['GET'])
def buscarProductoPorCodigo(codigo):
    return ProductoController.buscarPorCodigo(codigo)


# Actualizar cantidad de un producto
@pro_bp.route('/cantidad', methods=['PUT'])
def actualizarCantidadProducto():
    return ProductoController.actualizarCantidad()

pro_bp.add_url_rule(
    "/vista", view_func=ProductoController.vista_listar, methods=["GET"]
)
pro_bp.add_url_rule(
    "/vista/nuevo", view_func=ProductoController.vista_form, methods=["GET"]
)
pro_bp.add_url_rule(
    "/vista/nuevo", view_func=ProductoController.vista_crear, methods=["POST"]
)
