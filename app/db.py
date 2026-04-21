import sqlite3
import os


def create_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER,
        amount INTEGER
    )
    """)

    data = [
        (1, 100),
        (2, 250),
        (3, 300),
        (4, 400)
    ]

    cursor.execute("DELETE FROM orders")
    cursor.executemany("INSERT INTO orders VALUES (?, ?)", data)

    conn.commit()
    conn.close()


def get_db_data():
    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT order_id, amount FROM orders")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"order_id": row[0], "amount": row[1]}
        for row in rows
    ]


if __name__ == "__main__":
    create_db()