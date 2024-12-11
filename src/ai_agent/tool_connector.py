import requests

class ToolConnector:
    """Connects to external LLM APIs and other tools."""
    def __init__(self, config):
        self.endpoint = config.get('endpoint', 'http://localhost:8000/llm')
        self.api_key = config.get('api_key', '')
    
    def query_llm(self, prompt):
        payload = {"prompt": prompt, "api_key": self.api_key}
        response = requests.post(self.endpoint, json=payload)
        if response.status_code == 200:
    
    
    
    
    
    
    
    
    
