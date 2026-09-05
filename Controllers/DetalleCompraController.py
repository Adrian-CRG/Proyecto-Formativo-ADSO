from flask import jsonify, request
from Services.DetalleCompraService import DetalleCompraService


class DetalleCompraController:

    # Listar todos los detalles de compra
    def listar():
        data = DetalleCompraService.listar()
        return jsonify(data), 200


    # Crear un detalle de compra
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        comp_id = body.get("comp_id")
        pro_id = body.get("pro_id")
        cantidad = body.get("cantidad")
        precio = body.get("precio")
        fecha = body.get("fecha")
        factura = body.get("factura")

        # Validar campos obligatorios
        if comp_id is None or pro_id is None or cantidad is None or precio is None or fecha is None or factura is None:
            return jsonify({
                "error": "comp_id, pro_id, cantidad, precio, fecha y factura son obligatorios"
            }), 400

        # Validar comp_id
        try:
            comp_id = int(comp_id)

            if comp_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "comp_id debe ser un entero positivo"
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
        if not isinstance(cantidad, str) or not cantidad.strip():
            return jsonify({
                "error": "cantidad debe ser una cadena de texto válida"
            }), 400

        cantidad = cantidad.strip()

        # Validar precio
        try:
            precio = float(precio)

            if precio < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "precio debe ser un número mayor o igual a 0"
            }), 400

        # Validar fecha
        if not isinstance(fecha, str) or not fecha.strip():
            return jsonify({
                "error": "fecha debe ser una cadena de texto válida (YYYY-MM-DD)"
            }), 400

        fecha = fecha.strip()

        # Validar factura
        if not isinstance(factura, str) or not factura.strip():
            return jsonify({
                "error": "factura debe ser una cadena de texto válida"
            }), 400

        factura = factura.strip()

        # Verificar que no exista otra factura con el mismo número
        if DetalleCompraService.buscarPorFactura(factura) is not None:
            return jsonify({
                "error": "Ya existe un detalle de compra con esa factura"
            }), 409

        nuevo_detcom = DetalleCompraService.crear(
            comp_id, pro_id, cantidad, precio, fecha, factura
        )

        return jsonify(nuevo_detcom), 201


    # Actualizar un detalle de compra
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cantidad = body.get("cantidad")
        precio = body.get("precio")
        fecha = body.get("fecha")
        factura = body.get("factura")

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

        if not isinstance(cantidad, str) or not cantidad.strip():
            return jsonify({
                "error": "cantidad debe ser una cadena de texto válida"
            }), 400

        cantidad = cantidad.strip()

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

        # Validar factura
        if factura is None:
            return jsonify({
                "error": "factura es obligatorio"
            }), 400

        if not isinstance(factura, str) or not factura.strip():
            return jsonify({
                "error": "factura debe ser una cadena de texto válida"
            }), 400

        factura = factura.strip()

        # Verificar que no exista otro detalle con la misma factura
        detalle_existente = DetalleCompraService.buscarPorFactura(factura)

        if detalle_existente is not None and detalle_existente["id"] != id:
            return jsonify({
                "error": "Ya existe un detalle de compra con esa factura"
            }), 409

        filas_afectadas = DetalleCompraService.actualizar(
            id, cantidad, precio, fecha, factura
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Detalle de compra no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Detalle de compra actualizado correctamente"
        }), 200


    # Eliminar un detalle de compra
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

        filas_afectadas = DetalleCompraService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Detalle de compra no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Detalle de compra eliminado correctamente"
        }), 200


    # Listar por compra
    def listarPorCompra(comp_id):
        if comp_id is None:
            return jsonify({
                "error": "comp_id es obligatorio"
            }), 400

        try:
            comp_id = int(comp_id)

            if comp_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "comp_id debe ser un entero positivo"
            }), 400

        data = DetalleCompraService.listarPorCompra(comp_id)
        return jsonify(data), 200


    # Buscar por factura
    def buscarPorFactura(factura):
        if factura is None:
            return jsonify({
                "error": "factura es obligatorio"
            }), 400

        if not isinstance(factura, str) or not factura.strip():
            return jsonify({
                "error": "factura debe ser una cadena de texto válida"
            }), 400

        factura = factura.strip()
        detalle = DetalleCompraService.buscarPorFactura(factura)

        if detalle is None:
            return jsonify({
                "error": "Detalle de compra no encontrado"
            }), 404

        return jsonify(detalle), 200
