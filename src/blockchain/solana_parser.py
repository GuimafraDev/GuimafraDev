import json

class SolanaParser:
    """Parses raw Solana blockchain data."""
    def parse_transaction(self, tx_data):
        parsed = {}
        parsed['tx_id'] = tx_data.get('transaction', {}).get('signatures', [None])[0]
        parsed['instructions'] = tx_data.get('transaction', {}).get('message', {}).get('instructions', [])
        parsed['meta'] = tx_data.get('meta', {})
        return parsed
    
    def parse_wallet_info(self, wallet_data):
        info = {}
        info['wallet'] = wallet_data.get('address', '')
        info['balance'] = wallet_data.get('lamports', 0) / 1e9
        return info
    
    def batch_parse(self, data_list):
        results = []
        for data in data_list:







