from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    username = "abhishek"
    password = "123456"
    db_name="drmalpani"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{username}:{password}@localhost:5432/{db_name}"
    db.init_app(app)
    Migrate(app, db)
    from .views import views
    from .auth import auth
    app.register_blueprint(views , url_prifix="/")
    app.register_blueprint(auth , url_prifix="/")
    from .models import user     
    return app
