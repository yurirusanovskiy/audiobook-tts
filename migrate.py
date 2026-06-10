from db.database import engine
from sqlmodel import SQLModel
import sqlite3

def run():
    try:
        conn = sqlite3.connect("audiobook_core.db")
        cur = conn.cursor()
        cur.execute("ALTER TABLE sceneline ADD COLUMN phonetic_text VARCHAR;")
        conn.commit()
        conn.close()
        print("Added phonetic_text column")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("phonetic_text already exists")
        else:
            print("Error altering table:", e)
            
    SQLModel.metadata.create_all(engine)
    print("Database migrations complete")

if __name__ == "__main__":
    run()
