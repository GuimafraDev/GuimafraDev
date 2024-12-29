import yaml

class ConfigLoader:
    """Loads configuration from YAML files."""
    @staticmethod
    def load(path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                              
