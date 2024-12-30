import unittest
from src.blockchain.helius_connector import HeliusConnector
from src.blockchain.solana_parser import SolanaParser

class TestBlockchain(unittest.TestCase):
    """Tests for blockchain modules."""
    def setUp(self):
        self.connector = HeliusConnector('config/secrets_example.yaml')
        self.parser = SolanaParser()
    
    def test_parse_transaction(self):
        sample_tx = {
            "transaction": {
                "signatures": ["tx123"],
                "message": {"instructions": [{"data": "10"}]}
            },
            "meta": {}
        }
        parsed = self.parser.parse_transaction(sample_tx)
        self.assertEqual(parsed['tx_id'], "tx123")
    
    def test_get_wallet_transactions(self):
        txs = self.connector.get_wallet_transactions("dummy_wallet")
        self.assertIsInstance(txs, dict)

if __name__ == "__main__":
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
