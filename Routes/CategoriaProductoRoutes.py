from flask import Blueprint
from Controllers.CategoriaProductoController import CategoriaProductoController


catpro_bp = Blueprint('categoria_producto_bp', __name__)


# Listar todas las categorías de productos
@catpro_bp.route('/', methods=['GET'])
def listarCategoriasProductos():
    return CategoriaProductoController.listar()


# Crear una categoría de producto
@catpro_bp.route('/', methods=['POST'])
def crearCategoriaProducto():
    return CategoriaProductoController.crear()


# Eliminar una categoría de producto
@catpro_bp.route('/<int:id>', methods=['DELETE'])
def eliminarCategoriaProducto(id):
    return CategoriaProductoController.eliminar(id)


# Listar por producto
@catpro_bp.route('/producto/<int:pro_id>', methods=['GET'])
def listarPorProducto(pro_id):
    return CategoriaProductoController.listarPorProducto(pro_id)


# Listar por categoría
@catpro_bp.route('/categoria/<int:cat_id>', methods=['GET'])
def listarPorCategoria(cat_id):
    return CategoriaProductoController.listarPorCategoria(cat_id)
