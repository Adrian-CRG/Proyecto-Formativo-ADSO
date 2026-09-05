from flask import jsonify, request
from Services.DetalleInsumoService import DetalleInsumoService


class DetalleInsumoController:

    # Listar todos los detalles de insumo
    def listar():
        data = DetalleInsumoService.listar()
        return jsonify(data), 200


    # Crear un detalle de insumo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        cantidad_disp = body.get("cantidad_disp")
        proins_id = body.get("proins_id")
        ins_id = body.get("ins_id")

        # Validar campos obligatorios
        if cantidad_disp is None or proins_id is None or ins_id is None:
            return jsonify({
                "error": "cantidad_disp, proins_id e ins_id son obligatorios"
            }), 400

        # Validar cantidad_disp
        try:
            cantidad_disp = float(cantidad_disp)

            if cantidad_disp < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad_disp debe ser un número mayor o igual a 0"
            }), 400

        # Validar proins_id
        try:
            proins_id = int(proins_id)

            if proins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "proins_id debe ser un entero positivo"
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

        nuevo_detins = DetalleInsumoService.crear(
            cantidad_disp, proins_id, ins_id
        )

        return jsonify(nuevo_detins), 201


    # Actualizar un detalle de insumo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cantidad_disp = body.get("cantidad_disp")

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

        # Validar cantidad_disp
        if cantidad_disp is None:
            return jsonify({
                "error": "cantidad_disp es obligatorio"
            }), 400

        try:
            cantidad_disp = float(cantidad_disp)

            if cantidad_disp < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad_disp debe ser un número mayor o igual a 0"
            }), 400

        filas_afectadas = DetalleInsumoService.actualizar(id, cantidad_disp)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Detalle de insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Detalle de insumo actualizado correctamente"
        }), 200


    # Eliminar un detalle de insumo
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

        filas_afectadas = DetalleInsumoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Detalle de insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Detalle de insumo eliminado correctamente"
        }), 200


    # Listar por producto insumo
    def listarPorProductoInsumo(proins_id):
        if proins_id is None:
            return jsonify({
                "error": "proins_id es obligatorio"
            }), 400

        try:
            proins_id = int(proins_id)

            if proins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "proins_id debe ser un entero positivo"
            }), 400

        data = DetalleInsumoService.listarPorProductoInsumo(proins_id)
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

        data = DetalleInsumoService.listarPorInsumo(ins_id)
        return jsonify(data), 200
