import requests
import yaml

class HeliusConnector:
    """Connects to the Helius API for Solana blockchain data."""
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.api_key = self.config.get('api_keys', {}).get('helius', '')
        self.base_url = self.config.get('helius', {}).get('base_url', 'https://api.helius.xyz')
    
    def load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_wallet_transactions(self, wallet_address):
        url = f"{self.base_url}/wallets/{wallet_address}/transactions"
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return {}
    
    def get_transaction_details(self, tx_id):
        url = f"{self.base_url}/transactions/{tx_id}"
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return {}
    
    def monitor_wallet(self, wallet_address):
        transactions = self.get_wallet_transactions(wallet_address)
        return transactions