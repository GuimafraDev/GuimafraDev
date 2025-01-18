import sqlite3
import os

class Database:
    """Handles database connections."""
    def __init__(self, db_uri):
        self.db_uri = db_uri.replace('sqlite:///', '')
    
    def connect(self):
        return sqlite3.connect(self.db_uri)
    
    def execute_query(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
