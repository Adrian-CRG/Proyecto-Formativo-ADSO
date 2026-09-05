from flask import Blueprint
from Controllers.ProveedorController import ProveedorController


prov_bp = Blueprint('proveedor_bp', __name__)


# Listar todos los proveedores
@prov_bp.route('/', methods=['GET'])
def listarProveedores():
    return ProveedorController.listar()


# Buscar proveedor por código
@prov_bp.route('/codigo/<int:codigo>', methods=['GET'])
def buscarProveedorPorCodigo(codigo):
    return ProveedorController.buscarPorCodigo(codigo)


# Crear un proveedor
@prov_bp.route('/', methods=['POST'])
def crearProveedor():
    return ProveedorController.crear()


# Actualizar un proveedor
@prov_bp.route('/', methods=['PUT'])
def actualizarProveedor():
    return ProveedorController.actualizar()


# Eliminar un proveedor
@prov_bp.route('/<int:id>', methods=['DELETE'])
def eliminarProveedor(id):
    return ProveedorController.eliminar(id)
