import unittest
import networkx as nx
from src.graph_analysis.graph_builder import GraphBuilder
from src.graph_analysis.cluster_detection import ClusterDetection
from src.graph_analysis.labeling_strategies import LabelingStrategies

class TestGraphAnalysis(unittest.TestCase):
    """Tests for graph analysis modules."""
    def setUp(self):
        self.builder = GraphBuilder()
        sample_transactions = [
            {"source": "wallet_1", "destination": "wallet_2"},
            {"source": "wallet_2", "destination": "wallet_3"}
        ]
        self.graph = self.builder.build_from_transactions(sample_transactions)
        self.detector = ClusterDetection(self.graph)
        self.labeler = LabelingStrategies()
    
    def test_graph_construction(self):
        self.assertTrue(self.graph.has_node("wallet_1"))
        self.assertTrue(self.graph.has_edge("wallet_1", "wallet_2"))
    
    def test_cluster_detection(self):
        clusters = self.detector.detect_clusters()
        self.assertIsInstance(clusters, list)
    
    def test_labeling(self):
        label = self.labeler.combined_label({"balance": 1500, "trades": 20})
        self.assertIn(label, ["medium_profit_moderate", "low_profit_inactive", "high_profit_active"])

if __name__ == "__main__":
    unittest.main()