from flask import Flask
from config import Config
from config import enviro
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = enviro.get("SECRET_KEY")
    mail.init_app(app)

    from app.views.main import main
    app.register_blueprint(main)

    return app