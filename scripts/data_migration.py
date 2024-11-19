#!/usr/bin/env python3
import sqlite3
import yaml
import os
import sys
import pandas as pd

class DataMigrator:
    """Class for migrating data from legacy system to new database."""
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.source_file = self.config.get('migration', {}).get('source_file', 'legacy_data.csv')
        self.target_db = self.config.get('migration', {}).get('target_db', 'gods_eye.db')
    
    def load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def read_source_data(self):
        df = pd.read_csv(self.source_file)
        return df
    
    def transform_data(self, df):
        df = df.dropna()
        df.columns = [col.strip().lower() for col in df.columns]
        if 'wallet' in df.columns:
            df['wallet'] = df['wallet'].astype(str)
        return df
    
    def create_table(self, conn):
        create_sql = """
        CREATE TABLE IF NOT EXISTS legacy_wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet TEXT NOT NULL,
            balance REAL,
            strategy TEXT
        );
        """
        conn.execute(create_sql)
        conn.commit()
    
    def insert_data(self, conn, df):
        insert_sql = "INSERT INTO legacy_wallets (wallet, balance, strategy) VALUES (?, ?, ?)"
        for _, row in df.iterrows():
            conn.execute(insert_sql, (row.get('wallet'), row.get('balance', 0.0), row.get('strategy', 'unknown')))
        conn.commit()
    
    def migrate(self):
        df = self.read_source_data()
        df_transformed = self.transform_data(df)
        conn = sqlite3.connect(self.target_db)
        self.create_table(conn)
        self.insert_data(conn, df_transformed)
        conn.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: data_migration.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    migrator = DataMigrator(config_path)
    migrator.migrate()
    print("Data migration completed.")

if __name__ == "__main__":
    main()