#!/usr/bin/env python3
import sqlite3
import yaml
import os
import sys

class DatabaseSeeder:
    """Class for seeding the database with initial data."""
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.db_path = self.config.get('database', {}).get('uri', 'gods_eye.db').replace('sqlite:///', '')
    
    def load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def seed_wallets(self, conn):
        wallets = [
            ('wallet_1', 1000.0, 'scalping'),
            ('wallet_2', 2500.0, 'swing'),
            ('wallet_3', 500.0, 'arbitrage')
        ]
        insert_sql = "INSERT INTO legacy_wallets (wallet, balance, strategy) VALUES (?, ?, ?)"
        for wallet in wallets:
            conn.execute(insert_sql, wallet)
        conn.commit()
    
    def seed(self):
        conn = sqlite3.connect(self.db_path)
        self.seed_wallets(conn)
        conn.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: seed_database.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    seeder = DatabaseSeeder(config_path)
    seeder.seed()
    print("Database seeding completed.")

if __name__ == "__main__":
    main()