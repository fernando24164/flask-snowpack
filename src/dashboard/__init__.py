from flask import Flask, send_from_directory

from .api.blueprints.dashboard import dashboard_api
from .config import Config


def create_app():
    app = Flask(
        __name__,
        template_folder="../../build/",
        static_folder="../../build/ui",
    )
    app.config.from_object(Config)
    register_blueprints(app)
    register_endpoint_static(app)

    return app


def register_blueprints(app):
    app.register_blueprint(dashboard_api)


def register_endpoint_static(app):
    # Path for all the static files (compiled JS/CSS, etc.)
    @app.route("/<path:path>")
    def home(path):
        return send_from_directory("../../build/", path)
