from flask import jsonify, request
from Services.HistorialConsumoService import HistorialConsumoService


class HistorialConsumoController:

    # Listar todos los historiales de consumo
    def listar():
        data = HistorialConsumoService.listar()
        return jsonify(data), 200


    # Crear un historial de consumo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        consumo = body.get("consumo")
        disponibilidad = body.get("disponibilidad")
        prove_id = body.get("prove_id")
        detins_id = body.get("detins_id")

        # Validar campos obligatorios
        if consumo is None or disponibilidad is None or prove_id is None or detins_id is None:
            return jsonify({
                "error": "consumo, disponibilidad, prove_id y detins_id son obligatorios"
            }), 400

        # Validar consumo
        try:
            consumo = float(consumo)

            if consumo < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "consumo debe ser un número mayor o igual a 0"
            }), 400

        # Validar disponibilidad
        try:
            disponibilidad = float(disponibilidad)

            if disponibilidad < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "disponibilidad debe ser un número mayor o igual a 0"
            }), 400

        # Validar prove_id
        try:
            prove_id = int(prove_id)

            if prove_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "prove_id debe ser un entero positivo"
            }), 400

        # Validar detins_id
        try:
            detins_id = int(detins_id)

            if detins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "detins_id debe ser un entero positivo"
            }), 400

        nuevo_hiscon = HistorialConsumoService.crear(
            consumo, disponibilidad, prove_id, detins_id
        )

        return jsonify(nuevo_hiscon), 201


    # Actualizar un historial de consumo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        consumo = body.get("consumo")
        disponibilidad = body.get("disponibilidad")

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

        # Validar consumo
        if consumo is None:
            return jsonify({
                "error": "consumo es obligatorio"
            }), 400

        try:
            consumo = float(consumo)

            if consumo < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "consumo debe ser un número mayor o igual a 0"
            }), 400

        # Validar disponibilidad
        if disponibilidad is None:
            return jsonify({
                "error": "disponibilidad es obligatorio"
            }), 400

        try:
            disponibilidad = float(disponibilidad)

            if disponibilidad < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "disponibilidad debe ser un número mayor o igual a 0"
            }), 400

        filas_afectadas = HistorialConsumoService.actualizar(
            id, consumo, disponibilidad
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Historial de consumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Historial de consumo actualizado correctamente"
        }), 200


    # Eliminar un historial de consumo
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

        filas_afectadas = HistorialConsumoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Historial de consumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Historial de consumo eliminado correctamente"
        }), 200


    # Listar por proveedor insumo
    def listarPorProveedorInsumo(prove_id):
        if prove_id is None:
            return jsonify({
                "error": "prove_id es obligatorio"
            }), 400

        try:
            prove_id = int(prove_id)

            if prove_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "prove_id debe ser un entero positivo"
            }), 400

        data = HistorialConsumoService.listarPorProveedorInsumo(prove_id)
        return jsonify(data), 200


    # Listar por detalle insumo
    def listarPorDetalleInsumo(detins_id):
        if detins_id is None:
            return jsonify({
                "error": "detins_id es obligatorio"
            }), 400

        try:
            detins_id = int(detins_id)

            if detins_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "detins_id debe ser un entero positivo"
            }), 400

        data = HistorialConsumoService.listarPorDetalleInsumo(detins_id)
        return jsonify(data), 200
