import pandas as pd
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

    # Drop the table if it exists
    cur.execute("DROP TABLE IF EXISTS MAT")

    # Create the table
    cur.execute("""
    CREATE TABLE MAT (
        id SERIAL PRIMARY KEY,
        MarginAccountclientC VARCHAR(100),
        MarginAccountclientD VARCHAR(100),
        CollateralAccountclientC VARCHAR(100),
        CollateralAccountclientD VARCHAR(100),
        CollateralAccountmaisonC VARCHAR(100),
        CollateralAccountmaisonD VARCHAR(100),
        CommissionC VARCHAR(100),
        CommissionD VARCHAR(100),
        SettlementAccountclientC VARCHAR(100),
        SettlementAccountclientD VARCHAR(100),
        SettlementAccountmaisonC VARCHAR(100),
        SettlementAccountmaisonD VARCHAR(100)
    )
    """)
    conn.commit()
    conn.close()

def save_data_to_db(df):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Convert DataFrame values to native Python data types and handle missing values gracefully
    values = [df.loc[i, 'Crédit'] if i in df.index else None for i in range(1, 7)] + \
             [df.loc[i, 'Débit'] if i in df.index else None for i in range(1, 7)]
    values = [None if pd.isna(val) else str(val) for val in values]  # Convert to string and handle NaN values

    # Insert data into the table
    cur.execute("""
    INSERT INTO MAT (
        MarginAccountclientC, MarginAccountclientD, 
        CollateralAccountclientC, CollateralAccountclientD, 
        CollateralAccountmaisonC, CollateralAccountmaisonD, 
        CommissionC, CommissionD, 
        SettlementAccountclientC, SettlementAccountclientD,
        SettlementAccountmaisonC, SettlementAccountmaisonD
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, values)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database table created successfully.")

    # Load the second sheet
    file_path = 'file.xlsx'
    excel_data = pd.ExcelFile(file_path)
    second_sheet_name = excel_data.sheet_names[1]
    second_sheet_df = pd.read_excel(file_path, sheet_name=second_sheet_name)
    
    # Save the data to the database
    save_data_to_db(second_sheet_df)
    print("Data saved to database successfully.")

