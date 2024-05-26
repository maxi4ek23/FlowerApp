from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .bouquet_route import bouquet_bp
    from .catalogue_route import catalogue_bp
    from .flower_route import flower_bp
    from .order_route import order_bp
    from .packing_route import packing_bp
    from .user_route import user_bp
    from .bonus_card_route import bonus_card_bp


    app.register_blueprint(bouquet_bp)
    app.register_blueprint(catalogue_bp)
    app.register_blueprint(flower_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(packing_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(bonus_card_bp)