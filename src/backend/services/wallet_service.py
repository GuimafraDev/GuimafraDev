from ..models.wallet_model import WalletModel

class WalletService:
    """Service layer for wallet business logic."""
    def process_wallet(self, wallet_id):
        wallet = WalletModel.get(wallet_id)
        if wallet:
            wallet['processed'] = True
            WalletModel.update(wallet_id, wallet)
            return wallet
        return None
    
    def list_wallets(self):
        return WalletModel.get_all()