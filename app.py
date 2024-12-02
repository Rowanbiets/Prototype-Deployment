import logging
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route('/health', methods=['GET'])
    def health_check():
        app.logger.info("Health check endpoint was called.")
        return jsonify({"status": "healthy"}), 200

    @app.route('/add/<int:a>/<int:b>', methods=['GET'])
    def add_route(a, b):
        result = a + b
        app.logger.info(f"Addition endpoint called with {a} + {b} = {result}")
        return jsonify({"result": result})

    return app
