from flask import jsonify, request


def create_generic_routes(blueprint, controller, can_update):
    @blueprint.route('/', methods=['POST'])
    def create():
        instance, error = controller.create(request.json)
        response = instance if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @blueprint.route('/id/<int:_id>', methods=['GET'])
    def get_by_id(_id):
        instance, error = controller.get_by_id(_id)
        response = instance if not error else {'error': error}
        status_code = 200 if instance else 404 if not error else 400
        return jsonify(response), status_code

    @blueprint.route('/', methods=['GET'])
    def get_all():
        instances, error = controller.get_all()
        response = instances if not error else {'error': error}
        status_code = 200 if instances else 404 if not error else 400
        return jsonify(response), status_code
    
    if can_update:
        @blueprint.route('/', methods=['PUT'])
        def update():
            instance, error = controller.update(request.json)
            response = instance if not error else {'error': error}
            status_code = 200 if not error else 400
            return jsonify(response), status_code