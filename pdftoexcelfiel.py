import os
import tabula
from openpyxl import Workbook

def extract_tables_from_pdf(pdf_file):
    # Extract tables from PDF using tabula
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
    return tables

def save_tables_to_excel(tables, output_dir):
    # Create a new Excel workbook
    wb = Workbook()

    # Loop through each table and save it as a separate sheet
    for i, table in enumerate(tables):
        # Create a new sheet for the table
        sheet_name = f"Page_{i+1}"
        ws = wb.create_sheet(title=sheet_name)

        # Write the table data to the sheet
        for row in table.values:
            # Convert NumPy array to list before appending
            ws.append(list(row))

    # Remove the default sheet created by openpyxl
    wb.remove(wb['Sheet'])

    # Save the workbook to an Excel file
    excel_file = os.path.join(output_dir, os.path.splitext(os.path.basename(pdf_file))[0] + '.xlsx')
    wb.save(excel_file)

    print(f"Excel file saved: {excel_file}")



if __name__ == "__main__":
    # Input PDF file path
    pdf_file = 'file.pdf'

    # Output directory to save Excel files
    output_dir = 'output'

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract tables from PDF
    tables = extract_tables_from_pdf(pdf_file)

    # Save tables to Excel
    save_tables_to_excel(tables, output_dir)