from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from database import db


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)  # Always greater than 0
    color = db.Column(db.String(7))
    ppm_project_id = db.Column(db.String(7))


class ProjectsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Projects
        include_relationships = True
        load_instance = True
