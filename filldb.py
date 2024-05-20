import pandas as pd
import psycopg2

import pandas as pd
import psycopg2

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
    # Load the second sheet
    file_path = 'file.xlsx'
    excel_data = pd.ExcelFile(file_path)
    second_sheet_name = excel_data.sheet_names[1]
    second_sheet_df = pd.read_excel(file_path, sheet_name=second_sheet_name)
    
    # Save the data to the database
    save_data_to_db(second_sheet_df)
    print("Data saved to database successfully.")
