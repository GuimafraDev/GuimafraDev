from ..models.cluster_model import ClusterModel

class ClusterService:
    """Service layer for cluster business logic."""
    def process_cluster(self, cluster_id):
        cluster = ClusterModel.get(cluster_id)
        if cluster:
            cluster['processed'] = True
            ClusterModel.update(cluster_id, cluster)
            return cluster
        return None
    
    def list_clusters(self):
        return ClusterModel.get_all()
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
