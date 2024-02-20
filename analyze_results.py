import sqlite3


def analyze_experiment_results():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT name, status FROM experiments")
    experiments = c.fetchall()

    for experiment in experiments:
        print(f"Experiment: {experiment[0]}, Status: {experiment[1]}")

    conn.close()


if __name__ == "__main__":
    analyze_experiment_results()
