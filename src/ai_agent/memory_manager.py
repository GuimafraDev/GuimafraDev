import json
import os

class MemoryManager:
    """Manages conversation memory and historical interactions."""
    def __init__(self, config):
        self.memory_file = config.get('file', 'src/ai_agent/memory/memory_store.json')
        self.history_file = config.get('history', 'src/ai_agent/memory/conversation_history.json')
        self.memory = self.load_memory(self.memory_file)
        self.history = self.load_memory(self.history_file)
    
    def load_memory(self, filepath):
        if not os.path.exists(filepath):
            return {}
        with open(filepath, 'r') as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    
    def save_memory(self, data, filepath):
        with open(filepath, 'w') as f:
            json.dump(data, f)
    
    def store_interaction(self, input_data, prompt, response):
        entry = {"input": input_data, "prompt": prompt, "response": response}
        key = str(len(self.history))
        self.history[key] = entry
        self.save_memory(self.history, self.history_file)
    
    def recall(self, key):
        return self.history.get(key, None)
    
    def clear_memory(self):
        self.history = {}
        self.save_memory(self.history, self.history_file)