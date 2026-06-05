import sqlite3
class DatabaseManager:
    def __init__(self, db_name="gym_beast.db"): self.db_name = db_name
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: self.conn.commit()
        self.conn.close()
def initialize_schema():
    with DatabaseManager() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS workout_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, exercise_name TEXT, sets INTEGER, reps INTEGER, weight REAL, date_logged TEXT DEFAULT CURRENT_TIMESTAMP)')
        cursor.execute('CREATE TABLE IF NOT EXISTS personal_records (id INTEGER PRIMARY KEY AUTOINCREMENT, exercise_name TEXT UNIQUE, max_weight REAL, calculated_1rm REAL)')
      
