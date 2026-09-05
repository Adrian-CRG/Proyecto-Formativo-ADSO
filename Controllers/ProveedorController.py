from flask import jsonify, request
from Services.ProveedorService import ProveedorService


class ProveedorController:

    # Listar todos los proveedores
    def listar():
        data = ProveedorService.listar()
        return jsonify(data), 200


    # Buscar proveedor por código
    def buscarPorCodigo(codigo):
        if codigo is None:
            return jsonify({
                "error": "codigo es obligatorio"
            }), 400

        try:
            codigo = int(codigo)

            if codigo <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "codigo debe ser un entero positivo"
            }), 400

        proveedor = ProveedorService.buscarPorCodigo(codigo)

        if proveedor is None:
            return jsonify({
                "error": "Proveedor no encontrado"
            }), 404

        return jsonify(proveedor), 200


    # Crear un proveedor
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        codigo = body.get("codigo")
        nombre = body.get("nombre")

        # Validar campos obligatorios
        if codigo is None or nombre is None:
            return jsonify({
                "error": "codigo y nombre son obligatorios"
            }), 400

        # Validar codigo
        try:
            codigo = int(codigo)

            if codigo <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "codigo debe ser un entero positivo"
            }), 400

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            return jsonify({
                "error": "nombre debe ser una cadena de texto válida"
            }), 400

        nombre = nombre.strip()

        # Verificar que no exista otro proveedor con el mismo código
        if ProveedorService.buscarPorCodigo(codigo) is not None:
            return jsonify({
                "error": "Ya existe un proveedor con ese código"
            }), 409

        nuevo_proveedor = ProveedorService.crear(codigo, nombre)

        return jsonify(nuevo_proveedor), 201


    # Actualizar un proveedor
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        codigo = body.get("codigo")
        nombre = body.get("nombre")

        # Validar ID
        if id is None:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        try:
            id = int(id)

            if id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        # Validar codigo
        if codigo is None:
            return jsonify({
                "error": "codigo es obligatorio"
            }), 400

        try:
            codigo = int(codigo)

            if codigo <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "codigo debe ser un entero positivo"
            }), 400

        # Validar nombre
        if nombre is None:
            return jsonify({
                "error": "nombre es obligatorio"
            }), 400

        if not isinstance(nombre, str) or not nombre.strip():
            return jsonify({
                "error": "nombre debe ser una cadena de texto válida"
            }), 400

        nombre = nombre.strip()

        # Verificar que no exista otro proveedor con el mismo código
        proveedor_existente = ProveedorService.buscarPorCodigo(codigo)

        if proveedor_existente is not None and proveedor_existente["id"] != id:
            return jsonify({
                "error": "Ya existe un proveedor con ese código"
            }), 409

        filas_afectadas = ProveedorService.actualizar(id, codigo, nombre)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Proveedor no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Proveedor actualizado correctamente"
        }), 200


    # Eliminar un proveedor
    def eliminar(id):
        if id is None:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        try:
            id = int(id)

            if id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        filas_afectadas = ProveedorService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Proveedor no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Proveedor eliminado correctamente"
        }), 200
