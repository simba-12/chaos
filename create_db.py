import sqlite3


def create_database_and_settings():
    conn = sqlite3.connect('../test.db')
    c = conn.cursor()

    # Existing experiments table creation
    c.execute('''CREATE TABLE IF NOT EXISTS experiments
                 (id INTEGER PRIMARY KEY, name TEXT, status TEXT)''')

    # Create the settings table
    c.execute('''CREATE TABLE IF NOT EXISTS settings
                 (key TEXT PRIMARY KEY, value TEXT)''')

    # Insert the initial active database setting
    c.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('active_database', 'primary')")

    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()

    print("Database, table, and initial settings created successfully.")


if __name__ == "__main__":
    create_database_and_settings()
