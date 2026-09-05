from flask import jsonify, request
from Services.CategoriaProductoService import CategoriaProductoService


class CategoriaProductoController:

    # Listar todas las categorías de productos
    def listar():
        data = CategoriaProductoService.listar()
        return jsonify(data), 200


    # Crear una categoría de producto
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        pro_id = body.get("pro_id")
        cat_id = body.get("cat_id")

        # Validar campos obligatorios
        if pro_id is None or cat_id is None:
            return jsonify({
                "error": "pro_id y cat_id son obligatorios"
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

        # Validar cat_id
        try:
            cat_id = int(cat_id)

            if cat_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cat_id debe ser un entero positivo"
            }), 400

        nueva_catpro = CategoriaProductoService.crear(pro_id, cat_id)

        return jsonify(nueva_catpro), 201


    # Eliminar una categoría de producto
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

        filas_afectadas = CategoriaProductoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Categoría de producto no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Categoría de producto eliminada correctamente"
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

        data = CategoriaProductoService.listarPorProducto(pro_id)
        return jsonify(data), 200


    # Listar por categoría
    def listarPorCategoria(cat_id):
        if cat_id is None:
            return jsonify({
                "error": "cat_id es obligatorio"
            }), 400

        try:
            cat_id = int(cat_id)

            if cat_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cat_id debe ser un entero positivo"
            }), 400

        data = CategoriaProductoService.listarPorCategoria(cat_id)
        return jsonify(data), 200
