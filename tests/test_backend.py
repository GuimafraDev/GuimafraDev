import unittest
from src.backend.app import create_app

class TestBackend(unittest.TestCase):
    """Tests for the backend service."""
    def setUp(self):
        self.app = create_app('config/config.yaml').test_client()
    
    def test_healthcheck(self):
        response = self.app.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"status": "ok"', response.data)
    
    def test_wallet_routes(self):
        response = self.app.get('/wallets/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()