import sqlite3

DB_NAME = "test_results.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE test_failure (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            error_message TEXT NOT NULL,
            group_id INTEGER
        )
    """)
    db.commit()
    db.close()
