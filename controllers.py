from database import db
from models import Projects, ProjectsSchema


def hello_world():
    return 'Hello World!'


def create_project(project_name):
    db.session.add(Projects(name=project_name))
    db.session.commit()
    return ProjectsSchema(many=True).dump(Projects.query.all())


def get_projects():
    return ProjectsSchema(many=True).dump(Projects.query.all())


def get_project(project_id):
    return ProjectsSchema(many=True).dump(db.session.query(Projects).filter(Projects.id == project_id))


def get_project_by_name(project_name):
    return ProjectsSchema(many=True).dump(db.session.query(Projects).filter(Projects.name == project_name))


def delete_project_by_id(project_id):
    one_project = db.session.query(Projects).filter_by(id=project_id).one()
    db.session.delete(one_project)
    db.session.commit()
    return ProjectsSchema(many=True).dump(Projects.query.all())


def update_project(project_id, project_name, project_status, project_color):
    one_project = db.session.query(Projects).filter_by(id=project_id).one()
    one_project.name = project_name
    one_project.status = project_status or one_project.status
    one_project.color = project_color or one_project.color
    db.session.add(one_project)
    db.session.commit()
    return ProjectsSchema(many=True).dump(Projects.query.all())
