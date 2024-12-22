from flask import Blueprint, request, jsonify
from ..controllers.cluster_controller import ClusterController

cluster_bp = Blueprint('cluster_routes', __name__)
controller = ClusterController()

@cluster_bp.route('/', methods=['GET'])
def get_clusters():
    data = controller.get_all_clusters()
    return jsonify(data)

@cluster_bp.route('/<cluster_id>', methods=['GET'])
def get_cluster(cluster_id):
    data = controller.get_cluster(cluster_id)
    return jsonify(data)

@cluster_bp.route('/', methods=['POST'])
def create_cluster():
    cluster_data = request.get_json()
    data = controller.create_cluster(cluster_data)
    return jsonify(data), 201

@cluster_bp.route('/<cluster_id>', methods=['PUT'])
def update_cluster(cluster_id):
    cluster_data = request.get_json()
    data = controller.update_cluster(cluster_id, cluster_data)
    return jsonify(data)
                                     
                                     
                                     
                                     
                                     
                                     
                                     
