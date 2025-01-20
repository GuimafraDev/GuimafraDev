import yaml

class PromptManager:
    """Generates prompts for the AI Agent based on wallet data."""
    def __init__(self, config):
        self.prompts = config.get('definitions', {})
        self.default_prompt = config.get('default', 'Analyze the wallet data and provide insights.')
    
    def generate_prompt(self, wallet_data):
        if 'strategy' in wallet_data:
            prompt_template = self.prompts.get(wallet_data['strategy'], self.default_prompt)
        else:
            prompt_template = self.default_prompt
        prompt = prompt_template.format(**wallet_data)
        return prompt
    
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
