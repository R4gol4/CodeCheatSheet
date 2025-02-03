import sqlite3
import pandas as pd

DB_FILE = "commands.db"
EXCEL_FILE = "Common_Commands.xlsx"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS commands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        language TEXT NOT NULL,
        command TEXT NOT NULL,
        description TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def import_from_excel():
    df = pd.read_excel(EXCEL_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("INSERT INTO commands (language, command, description) VALUES (?, ?, ?)",
                       (row['Language'], row['Command'], row['Description']))

    conn.commit()
    conn.close()
    print("✅ Database populated successfully!")

# Run the setup
create_database()
import_from_excel()
