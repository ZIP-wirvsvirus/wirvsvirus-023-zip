import os

from flask import Flask
from config import Config
from database.db import db

from api.endpoint import endpoint


@app.route('/')
def hello_world():
    return 'Hello World!'


def main(cfg=Config):
    app = Flask(__name__)
    app.config.from_object(cfg)  # Choose from the different configs...
    db.init_app(app)
    app.register_blueprint(endpoint)
    return app


app = main()

if __name__ == "__main__":
    app = main()
    port = int(os.environ.get("API_PORT", 80))
    app.run(host=os.environ.get("API_IP", "0.0.0.0"), port=port)
