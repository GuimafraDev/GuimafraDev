import os
import yaml
from .prompt_manager import PromptManager
from .memory_manager import MemoryManager
from .tool_connector import ToolConnector

class Agent:
    """AI Agent for processing on-chain data and interacting with LLM."""
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.prompt_manager = PromptManager(self.config.get('prompts', {}))
        self.memory_manager = MemoryManager(self.config.get('memory', {}))
        self.tool_connector = ToolConnector(self.config.get('tools', {}))
    
    def load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def process_wallet(self, wallet_data):
        prompt = self.prompt_manager.generate_prompt(wallet_data)
        result = self.tool_connector.query_llm(prompt)
        self.memory_manager.store_interaction(wallet_data, prompt, result)
        return result
    
    def analyze_network(self, network_data):
        analysis = {}
        for wallet in network_data:
            analysis[wallet] = self.process_wallet(network_data[wallet])
        return analysis
    
    def run(self, data_source):
        results = {}
        for wallet, data in data_source.items():
            results[wallet] = self.process_wallet(data)
        return results

def main():
    config_path = os.environ.get('AGENT_CONFIG', 'src/ai_agent/configs/agent_config.yaml')
    agent = Agent(config_path)
    sample_data = {
        "wallet_1": {"balance": 1000, "trades": 10},
        "wallet_2": {"balance": 2500, "trades": 25}
    }
    results = agent.run(sample_data)
    print("Agent analysis results:")
    for wallet, res in results.items():
        print(f"{wallet}: {res}")

if __name__ == "__main__":
    main()