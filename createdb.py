import psycopg2

def create_table():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS MAT (
        id SERIAL PRIMARY KEY,
        MarginAccountclientC VARCHAR(100),
        MarginAccountclientD VARCHAR(100),
        MarginAccountmaisonC VARCHAR(100),
        MarginAccountmaisonD VARCHAR(100),
        CollateralAccountclientC VARCHAR(100),
        CollateralAccountclientD VARCHAR(100),
        CollateralAccountmaisonC VARCHAR(100),
        CollateralAccountmaisonD VARCHAR(100),
        CommissionC VARCHAR(100),
        CommissionD VARCHAR(100),
        SettlementAccountclientC VARCHAR(100),
        SettlementAccountclientD VARCHAR(100)
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database table created successfully.")
