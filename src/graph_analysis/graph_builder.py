import networkx as nx

class GraphBuilder:
    """Builds a graph of wallet interconnections."""
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_wallet(self, wallet):
        self.graph.add_node(wallet)
    
    def add_connection(self, wallet_a, wallet_b, weight=1):
        self.graph.add_edge(wallet_a, wallet_b, weight=weight)
    
    def build_from_transactions(self, transactions):
        for tx in transactions:
            src = tx.get('source')
            dst = tx.get('destination')
            if src and dst:
                self.add_wallet(src)
                self.add_wallet(dst)
                if self.graph.has_edge(src, dst):
                    self.graph[src][dst]['weight'] += 1
                else:
                    self.add_connection(src, dst)
        return self.graph
    
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
                                                 
