from  pdftoexcelfiel import  extract_tables_from_pdf , save_tables_to_excel
import os 
pdf_file = 'Règles de compensation.pdf'

    # Output directory to save Excel files
output_dir = 'output'

    # Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

    # Extract tables from PDF
    tables = extract_tables_from_pdf(pdf_file)

    # Save tables to Excel
    save_tables_to_excel(tables, output_dir)
