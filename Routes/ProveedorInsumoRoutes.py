from flask import Blueprint
from Controllers.ProveedorInsumoController import ProveedorInsumoController


prove_bp = Blueprint('proveedor_insumo_bp', __name__)


# Listar todos los proveedores de insumos
@prove_bp.route('/', methods=['GET'])
def listarProveedoresInsumos():
    return ProveedorInsumoController.listar()


# Crear un proveedor de insumo
@prove_bp.route('/', methods=['POST'])
def crearProveedorInsumo():
    return ProveedorInsumoController.crear()


# Actualizar un proveedor de insumo
@prove_bp.route('/', methods=['PUT'])
def actualizarProveedorInsumo():
    return ProveedorInsumoController.actualizar()


# Eliminar un proveedor de insumo
@prove_bp.route('/<int:id>', methods=['DELETE'])
def eliminarProveedorInsumo(id):
    return ProveedorInsumoController.eliminar(id)


# Listar por proveedor
@prove_bp.route('/proveedor/<int:prov_id>', methods=['GET'])
def listarPorProveedor(prov_id):
    return ProveedorInsumoController.listarPorProveedor(prov_id)


# Listar por insumo
@prove_bp.route('/insumo/<int:ins_id>', methods=['GET'])
def listarPorInsumo(ins_id):
    return ProveedorInsumoController.listarPorInsumo(ins_id)
