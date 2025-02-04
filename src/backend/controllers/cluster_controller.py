from ..models.cluster_model import ClusterModel

class ClusterController:
    """Controller for cluster operations."""
    def get_all_clusters(self):
        return ClusterModel.get_all()
    
    def get_cluster(self, cluster_id):
        return ClusterModel.get(cluster_id)
    
    def create_cluster(self, cluster_data):
        return ClusterModel.create(cluster_data)
    
    def update_cluster(self, cluster_id, cluster_data):
        return ClusterModel.update(cluster_id, cluster_data)
                                           
                                           
                                           
                                           
                                           
                                           
    
    
    
    
    
    
    
    
    
    
