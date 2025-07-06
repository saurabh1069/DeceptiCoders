
from flask import Flask
import logging
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Ensure logs directory exists
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'app.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s'
    )

    from .routes import setup_routes
    setup_routes(app)
    return app