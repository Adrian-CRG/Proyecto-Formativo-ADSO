from flask import jsonify, request
from Services.ProductoInsumoService import ProductoInsumoService


class ProductoInsumoController:

    # Listar todos los productos insumos
    def listar():
        data = ProductoInsumoService.listar()
        return jsonify(data), 200


    # Crear un producto insumo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        pro_id = body.get("pro_id")
        cantidad = body.get("cantidad")
        fecha_fabricacion = body.get("fecha_fabricacion")

        # Validar campos obligatorios
        if pro_id is None or cantidad is None or fecha_fabricacion is None:
            return jsonify({
                "error": "pro_id, cantidad y fecha_fabricacion son obligatorios"
            }), 400

        # Validar pro_id
        try:
            pro_id = int(pro_id)

            if pro_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "pro_id debe ser un entero positivo"
            }), 400

        # Validar cantidad
        try:
            cantidad = float(cantidad)

            if cantidad < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad debe ser un número mayor o igual a 0"
            }), 400

        # Validar fecha_fabricacion
        if not isinstance(fecha_fabricacion, str) or not fecha_fabricacion.strip():
            return jsonify({
                "error": "fecha_fabricacion debe ser una cadena de texto válida (YYYY-MM-DD)"
            }), 400

        fecha_fabricacion = fecha_fabricacion.strip()

        nuevo_proins = ProductoInsumoService.crear(
            pro_id, cantidad, fecha_fabricacion
        )

        return jsonify(nuevo_proins), 201


    # Actualizar un producto insumo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cantidad = body.get("cantidad")
        fecha_fabricacion = body.get("fecha_fabricacion")

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

        # Validar fecha_fabricacion
        if fecha_fabricacion is None:
            return jsonify({
                "error": "fecha_fabricacion es obligatorio"
            }), 400

        if not isinstance(fecha_fabricacion, str) or not fecha_fabricacion.strip():
            return jsonify({
                "error": "fecha_fabricacion debe ser una cadena de texto válida (YYYY-MM-DD)"
            }), 400

        fecha_fabricacion = fecha_fabricacion.strip()

        filas_afectadas = ProductoInsumoService.actualizar(
            id, cantidad, fecha_fabricacion
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto insumo actualizado correctamente"
        }), 200


    # Eliminar un producto insumo
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

        filas_afectadas = ProductoInsumoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto insumo eliminado correctamente"
        }), 200


    # Listar por producto
    def listarPorProducto(pro_id):
        if pro_id is None:
            return jsonify({
                "error": "pro_id es obligatorio"
            }), 400

        try:
            pro_id = int(pro_id)

            if pro_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "pro_id debe ser un entero positivo"
            }), 400

        data = ProductoInsumoService.listarPorProducto(pro_id)
        return jsonify(data), 200
