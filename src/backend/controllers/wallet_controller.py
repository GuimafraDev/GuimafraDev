from ..models.wallet_model import WalletModel

class WalletController:
    """Controller for wallet operations."""
    def get_all_wallets(self):
        return WalletModel.get_all()
    
    def get_wallet(self, wallet_id):
        return WalletModel.get(wallet_id)
    
    def create_wallet(self, wallet_data):
        return WalletModel.create(wallet_data)
    
    def update_wallet(self, wallet_id, wallet_data):
        return WalletModel.update(wallet_id, wallet_data)
                                           
                                           
                                           
                                           
                                           
                                           
                                    
                                    
                                    
                                    
                                    
                                    
