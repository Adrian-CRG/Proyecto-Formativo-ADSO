from flask import jsonify, request
from Services.ProveedorInsumoService import ProveedorInsumoService


class ProveedorInsumoController:

    # Listar todos los proveedores de insumos
    def listar():
        data = ProveedorInsumoService.listar()
        return jsonify(data), 200


    # Crear un proveedor de insumo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        ins_id = body.get("ins_id")
        prov_id = body.get("prov_id")
        fecha = body.get("fecha")
        cantidad = body.get("cantidad")
        precio = body.get("precio")
        tipo_insumo = body.get("tipo_insumo")

        # Validar campos obligatorios
        if ins_id is None or prov_id is None or fecha is None or cantidad is None or precio is None or tipo_insumo is None:
            return jsonify({
                "error": "ins_id, prov_id, fecha, cantidad, precio y tipo_insumo son obligatorios"
            }), 400

        # Validar ins_id
        try:
            ins_id = int(ins_id)

            if ins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "ins_id debe ser un entero positivo"
            }), 400

        # Validar prov_id
        try:
            prov_id = int(prov_id)

            if prov_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "prov_id debe ser un entero positivo"
            }), 400

        # Validar fecha
        if not isinstance(fecha, str) or not fecha.strip():
            return jsonify({
                "error": "fecha debe ser una cadena de texto válida (YYYY-MM-DD)"
            }), 400

        fecha = fecha.strip()

        # Validar cantidad
        try:
            cantidad = float(cantidad)

            if cantidad < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad debe ser un número mayor o igual a 0"
            }), 400

        # Validar precio
        try:
            precio = float(precio)

            if precio < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "precio debe ser un número mayor o igual a 0"
            }), 400

        # Validar tipo_insumo
        if not isinstance(tipo_insumo, str) or not tipo_insumo.strip():
            return jsonify({
                "error": "tipo_insumo debe ser una cadena de texto válida"
            }), 400

        tipo_insumo = tipo_insumo.strip()

        nuevo_prove = ProveedorInsumoService.crear(
            ins_id, prov_id, fecha, cantidad, precio, tipo_insumo
        )

        return jsonify(nuevo_prove), 201


    # Actualizar un proveedor de insumo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        fecha = body.get("fecha")
        cantidad = body.get("cantidad")
        precio = body.get("precio")
        tipo_insumo = body.get("tipo_insumo")

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

        # Validar fecha
        if fecha is None:
            return jsonify({
                "error": "fecha es obligatorio"
            }), 400

        if not isinstance(fecha, str) or not fecha.strip():
            return jsonify({
                "error": "fecha debe ser una cadena de texto válida (YYYY-MM-DD)"
            }), 400

        fecha = fecha.strip()

        # Validar cantidad
        if cantidad is None:
            return jsonify({
                "error": "cantidad es obligatorio"
            }), 400

        try:
            cantidad = float(cantidad)

            if cantidad < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad debe ser un número mayor o igual a 0"
            }), 400

        # Validar precio
        if precio is None:
            return jsonify({
                "error": "precio es obligatorio"
            }), 400

        try:
            precio = float(precio)

            if precio < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "precio debe ser un número mayor o igual a 0"
            }), 400

        # Validar tipo_insumo
        if tipo_insumo is None:
            return jsonify({
                "error": "tipo_insumo es obligatorio"
            }), 400

        if not isinstance(tipo_insumo, str) or not tipo_insumo.strip():
            return jsonify({
                "error": "tipo_insumo debe ser una cadena de texto válida"
            }), 400

        tipo_insumo = tipo_insumo.strip()

        filas_afectadas = ProveedorInsumoService.actualizar(
            id, fecha, cantidad, precio, tipo_insumo
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Proveedor insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Proveedor insumo actualizado correctamente"
        }), 200


    # Eliminar un proveedor de insumo
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

        filas_afectadas = ProveedorInsumoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Proveedor insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Proveedor insumo eliminado correctamente"
        }), 200


    # Listar por proveedor
    def listarPorProveedor(prov_id):
        if prov_id is None:
            return jsonify({
                "error": "prov_id es obligatorio"
            }), 400

        try:
            prov_id = int(prov_id)

            if prov_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "prov_id debe ser un entero positivo"
            }), 400

        data = ProveedorInsumoService.listarPorProveedor(prov_id)
        return jsonify(data), 200


    # Listar por insumo
    def listarPorInsumo(ins_id):
        if ins_id is None:
            return jsonify({
                "error": "ins_id es obligatorio"
            }), 400

        try:
            ins_id = int(ins_id)

            if ins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "ins_id debe ser un entero positivo"
            }), 400

        data = ProveedorInsumoService.listarPorInsumo(ins_id)
        return jsonify(data), 200
