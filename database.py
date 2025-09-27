import sqlite3
import pandas as pd
from datetime import datetime
import os

class Database:
    def __init__(self, db_path="pet_health.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Create all necessary tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Pets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                species TEXT NOT NULL,
                breed TEXT,
                age INTEGER,
                weight REAL,
                color TEXT,
                owner_name TEXT NOT NULL,
                owner_phone TEXT,
                owner_email TEXT,
                owner_address TEXT,
                microchip_id TEXT UNIQUE,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP,
                qr_code TEXT,
                photo_path TEXT,
                medical_conditions TEXT,
                is_lost INTEGER DEFAULT 0,
                last_seen_location TEXT,
                lost_date TEXT
            )
        ''')

        # Medical records table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medical_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_id INTEGER,
                visit_date TEXT NOT NULL,
                veterinarian TEXT,
                clinic_name TEXT,
                diagnosis TEXT,
                treatment TEXT,
                medications TEXT,
                next_visit_date TEXT,
                notes TEXT,
                cost REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (pet_id) REFERENCES pets (id)
            )
        ''')

        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")

    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            conn.close()
            return pd.DataFrame(results, columns=columns) if results else pd.DataFrame()
        else:
            conn.commit()
            lastrowid = cursor.lastrowid
            conn.close()
            return lastrowid

    def insert_pet(self, pet_data):
        """Insert a new pet record"""
        query = '''
            INSERT INTO pets (name, species, breed, age, weight, color, 
                            owner_name, owner_phone, owner_email, owner_address,
                            microchip_id, qr_code, photo_path, medical_conditions)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        return self.execute_query(query, pet_data)

    def get_all_pets(self):
        """Get all registered pets"""
        query = "SELECT * FROM pets ORDER BY registration_date DESC"
        return self.execute_query(query)

    def get_statistics(self):
        """Get various statistics for dashboard"""
        stats = {}

        # Total pets
        result = self.execute_query("SELECT COUNT(*) as count FROM pets")
        stats['total_pets'] = result.iloc[0]['count'] if not result.empty else 0

        # Lost pets
        result = self.execute_query("SELECT COUNT(*) as count FROM pets WHERE is_lost = 1")
        stats['lost_pets'] = result.iloc[0]['count'] if not result.empty else 0

        # Recent registrations (last 30 days)
        result = self.execute_query(
            "SELECT COUNT(*) as count FROM pets WHERE DATE(registration_date) >= DATE('now', '-30 days')"
        )
        stats['recent_registrations'] = result.iloc[0]['count'] if not result.empty else 0

        # Medical records count
        result = self.execute_query("SELECT COUNT(*) as count FROM medical_records")
        stats['medical_records'] = result.iloc[0]['count'] if not result.empty else 0

        return stats
