import json
import os

class ReportGenerator:
    """Generates reports on detected clusters and wallet labels."""
    def __init__(self, output_path="reports/report.json"):
        self.output_path = output_path
    
    def generate_report(self, clusters, labels, analytics):
        report = {
            "clusters": clusters,
            "labels": labels,
            "analytics": analytics
        }
        self.save_report(report)
        return report
    
    def save_report(self, report):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        with open(self.output_path, 'w') as f:
            json.dump(report, f, indent=2)
    
    def load_report(self):
        with open(self.output_path, 'r') as f:
            return json.load(f)
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
