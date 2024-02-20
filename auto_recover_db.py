# auto_recover_db.py
import sqlite3
import time


def auto_recover_database():
    time.sleep(60)  # Wait for 60 seconds before auto-recovery
    conn = sqlite3.connect('../test.db')
    c = conn.cursor()
    c.execute("UPDATE settings SET value='primary' WHERE key='active_database'")
    conn.commit()
    conn.close()
    print("Database auto-recovery completed. Active database switched to: primary")


if __name__ == "__main__":
    auto_recover_database()
