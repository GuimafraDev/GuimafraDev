import unittest
import json
from src.backend.app import create_app

class TestEndToEnd(unittest.TestCase):
    """End-to-end tests for the God's Eye service."""
    def setUp(self):
        self.app = create_app('config/config.yaml').test_client()
    
    def test_full_workflow(self):
        wallet_payload = {"wallet": "wallet_test", "balance": 2000, "trades": 15}
        post_response = self.app.post('/wallets/', json=wallet_payload)
        self.assertEqual(post_response.status_code, 201)
        get_response = self.app.get('/wallets/')
        data = json.loads(get_response.data)
        self.assertTrue(any(w.get('wallet') == "wallet_test" for w in data))
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
