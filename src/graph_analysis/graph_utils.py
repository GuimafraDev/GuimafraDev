import networkx as nx

class GraphUtils:
    """Utility functions for graph analysis."""
    def __init__(self, graph):
        self.graph = graph
    
    def shortest_path(self, source, target):
        try:
            path = nx.shortest_path(self.graph, source=source, target=target)
            return path
        except nx.NetworkXNoPath:
            return []
    
    def centrality_measures(self):
        degree = nx.degree_centrality(self.graph)
    
    
    
    
                              
                              
                              
                              
                              
