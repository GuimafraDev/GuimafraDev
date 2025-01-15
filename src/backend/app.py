from flask import Flask, request, jsonify
import yaml
import os
from .routes.wallet_routes import wallet_bp
from .routes.cluster_routes import cluster_bp
from .routes.healthcheck import health_bp
from .services.utils.config_loader import ConfigLoader

def create_app(config_path=None):
    app = Flask(__name__)
    if config_path is None:
        config_path = os.environ.get('CONFIG_PATH', 'config/config.yaml')
    config = ConfigLoader.load(config_path)
    app.config.update(config)
    app.register_blueprint(wallet_bp, url_prefix='/wallets')
    app.register_blueprint(cluster_bp, url_prefix='/clusters')
    app.register_blueprint(health_bp, url_prefix='/health')
    return app

def main():
    app = create_app()
    app.run(host=app.config.get('app', {}).get('host', '0.0.0.0'),
            port=app.config.get('app', {}).get('port', 5000))














                                                      
                                                      
                                                      
