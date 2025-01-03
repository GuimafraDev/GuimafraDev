class ClusterModel:
    """Represents a cluster of wallets."""
    _db = {}

    @classmethod
    def create(cls, cluster_data):
        cluster_id = str(len(cls._db) + 1)
        cls._db[cluster_id] = cluster_data
        cls._db[cluster_id]['id'] = cluster_id
        return cls._db[cluster_id]
    
    @classmethod
    def get(cls, cluster_id):
        return cls._db.get(cluster_id)
    
    @classmethod
    def get_all(cls):
        return list(cls._db.values())
    
    @classmethod
    def update(cls, cluster_id, cluster_data):
        if cluster_id in cls._db:
            cls._db[cluster_id].update(cluster_data)
                   
                   
                   
                   
                   
                   
                   
