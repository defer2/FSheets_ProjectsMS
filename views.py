from flask import Blueprint, jsonify, request
import controllers
from flask_cors import CORS, cross_origin

view_blueprint = Blueprint('view_blueprint', __name__)


@view_blueprint.route('/', methods=['GET'])
@cross_origin()
def hello_world():
    return controllers.hello_world()


@view_blueprint.route('/create', methods=['POST'])
@cross_origin()
def create_project():
    project_name = request.args.get("name")
    project_color = request.args.get("color")
    return jsonify(controllers.create_project(project_name, project_color))


@view_blueprint.route('/view', methods=['GET'])
@cross_origin()
def get_projects():
    return jsonify(controllers.get_projects())


@view_blueprint.route('/view/<int:project_id>', methods=['GET'])
@cross_origin()
def get_project(project_id):
    return jsonify(controllers.get_project(project_id))


@view_blueprint.route('/view/<string:project_name>', methods=['GET'])
@cross_origin()
def get_project_by_name(project_name):
    return jsonify(controllers.get_project_by_name(project_name))


@view_blueprint.route('/delete/<int:project_id>', methods=['DELETE'])
@cross_origin()
def delete_project_by_id(project_id):
    return jsonify(controllers.delete_project_by_id(project_id))


@view_blueprint.route('/update/<int:project_id>', methods=['PUT'])
@cross_origin()
def update_project(project_id):
    project_name = request.args.get("name")
    project_status = request.args.get("status")
    project_color = request.args.get("color")
    ppm_project_id = request.args.get("ppm_project_id")
    return jsonify(controllers.update_project(project_id, project_name, project_status, project_color, ppm_project_id))
