import sqlite3


def check_active_database():
    """Check and print the current active database setting."""
    conn = sqlite3.connect('../test.db')  # Ensure this matches your database file
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key='active_database'")
    active_db = c.fetchone()[0]  # Fetch the first row's first column
    print(f"Current active database is: {active_db}")

    conn.close()


if __name__ == "__main__":
    check_active_database()
