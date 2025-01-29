import networkx as nx

class ClusterDetection:
    """Detects clusters of interconnected wallets."""
    def __init__(self, graph):
        self.graph = graph
    
    def detect_clusters(self):
        clusters = list(nx.connected_components(self.graph))
        return clusters
    
    def label_clusters(self, clusters):
        labeled = {}
        for idx, cluster in enumerate(clusters):
            label = f"cluster_{idx+1}"
            for wallet in cluster:
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     






