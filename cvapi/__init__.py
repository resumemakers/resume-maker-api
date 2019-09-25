from flask import Flask, jsonify, request
from .schema import ResumeSchema, configure_app
from marshmallow.exceptions import ValidationError


def create_app():
    app = Flask(__name__)
    configure_app(app)

    @app.route('/validate-json', methods=['POST'])
    def validate_json():
        try:
            ResumeSchema().load(request.json)
            return jsonify({'ok': 'Dados válidos'}), 201
        except ValidationError as m_error:
            return jsonify(m_error.normalized_messages()), 400

    return app
