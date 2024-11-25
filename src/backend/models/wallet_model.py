class WalletModel:
    """Represents a wallet in the system."""
    _db = {}

    @classmethod
    def create(cls, wallet_data):
        wallet_id = str(len(cls._db) + 1)
        cls._db[wallet_id] = wallet_data
        cls._db[wallet_id]['id'] = wallet_id
        return cls._db[wallet_id]
    
    @classmethod
    def get(cls, wallet_id):
        return cls._db.get(wallet_id)
    
    @classmethod
    def get_all(cls):
        return list(cls._db.values())
    
    @classmethod
    def update(cls, wallet_id, wallet_data):
        if wallet_id in cls._db:
            cls._db[wallet_id].update(wallet_data)
            return cls._db[wallet_id]
        return None