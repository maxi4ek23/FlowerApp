import os
import secrets
from typing import Dict, Any

from flask_socketio import SocketIO, emit
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS

# from .util.observer.packing_observer import PackingObserver, PackingSubject
from .route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*")

def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    CORS(app)
    socketio.init_app(app)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}
    app.json.sort_keys = False

    # @socketio.on('connect')
    # def handle_connect():
    #     sid = request.sid
    #     observer_id = request.args.get('observer_id')
    #     observer = PackingObserver(observer_id, sid)
    #     PackingSubject.add_observer(observer)
    #     print(f'Client {observer_id} connected and registered as observer with sid {sid}')

    # @socketio.on('disconnect')
    # def handle_disconnect():
    #     sid = request.sid
    #     observer_id = request.args.get('observer_id')
    #     PackingSubject.remove_observer(observer_id)
    #     print(f'Client {observer_id} disconnected and unregistered as observer with sid {sid}')


    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import flower_store.model
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    # Set root username and password in app_config
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
