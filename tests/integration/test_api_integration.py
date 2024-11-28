import unittest
import json
from src.backend.app import create_app

class TestAPIIntegration(unittest.TestCase):
    """API integration tests for the God's Eye service."""
    def setUp(self):
        self.app = create_app('config/config.yaml').test_client()
    
    def test_wallet_creation_and_retrieval(self):
        payload = {"wallet": "wallet_integration", "balance": 3000, "trades": 5}
        post_resp = self.app.post('/wallets/', json=payload)
        self.assertEqual(post_resp.status_code, 201)
        get_resp = self.app.get('/wallets/')
        wallets = json.loads(get_resp.data)
        self.assertTrue(any(w.get('wallet') == "wallet_integration" for w in wallets))

if __name__ == "__main__":
    unittest.main()