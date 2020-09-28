import os.path
from flask import Flask
from database import db
from views import view_blueprint
from flask_cors import CORS



def create_app():
    app_projects = Flask(__name__)
    app_projects.config['DEBUG'] = True
    app_projects.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/projects.db'
    app_projects.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_projects.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app_projects)
    app_projects.register_blueprint(view_blueprint, url_prefix='')
    return app_projects


def setup_database(app_projects):
    with app_projects.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app()
    cors = CORS(app)

    if not os.path.isfile('database/projects.db'):
        setup_database(app)

    app.run(host='192.168.0.50', port=5010)
