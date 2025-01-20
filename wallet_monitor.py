import time
from .helius_connector import HeliusConnector

class WalletMonitor:
    """Monitors wallets for high profit activity."""
    def __init__(self, config_path):
        self.connector = HeliusConnector(config_path)
        self.monitored_wallets = []
    
    def add_wallet(self, wallet_address):
        if wallet_address not in self.monitored_wallets:
            self.monitored_wallets.append(wallet_address)
    
    def remove_wallet(self, wallet_address):
        if wallet_address in self.monitored_wallets:
            self.monitored_wallets.remove(wallet_address)
    
    def monitor(self, interval=10):
        results = {}
        for wallet in self.monitored_wallets:
            tx_data = self.connector.get_wallet_transactions(wallet)
            results[wallet] = tx_data
        return results
    
    def continuous_monitor(self, interval=30):
        while True:
            data = self.monitor()
            print("Monitoring data:", data)
            time.sleep(interval)