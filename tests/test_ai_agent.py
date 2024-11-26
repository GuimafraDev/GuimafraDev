import unittest
import os
from src.ai_agent.agent import Agent

class TestAIAgent(unittest.TestCase):
    """Tests for the AI Agent."""
    def setUp(self):
        os.environ['AGENT_CONFIG'] = 'src/ai_agent/configs/agent_config.yaml'
        self.agent = Agent(os.environ['AGENT_CONFIG'])
    
    def test_process_wallet(self):
        wallet_data = {"balance": 1500, "trades": 20, "strategy": "scalping"}
        result = self.agent.process_wallet(wallet_data)
        self.assertIsInstance(result, str)
    
    def test_analyze_network(self):
        network_data = {
            "wallet_1": {"balance": 1000, "trades": 10, "strategy": "swing"},
            "wallet_2": {"balance": 2000, "trades": 30, "strategy": "arbitrage"}
        }
        analysis = self.agent.analyze_network(network_data)
        self.assertEqual(len(analysis), 2)

if __name__ == "__main__":
    unittest.main()