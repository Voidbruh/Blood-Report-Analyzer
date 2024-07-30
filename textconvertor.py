import pdfplumber
import pandas as pd

def tables_from_pdf(pdf_path):
    """Extracts tables from a PDF using pdfplumber."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            tables = first_page.extract_tables()
            print(tables)
            return tables
    except Exception as e:
        print(f"Error occurred while extracting tables from PDF: {e}")
        return None

def table_to_text(tables):
    """Converts the extracted tables into a readable text format."""
    if tables is None:
        return "No tables found in the PDF."

    text = ""
    header_printed = False  # Flag to track if the header is printed
    for table in tables:
        df = pd.DataFrame(table[1:], columns=table[0])
        # Check if the table is not empty
        if not df.empty:
            if not header_printed:
                text += df.columns[0] + ": "
                header_printed = True
                text += "\n"
            for _, row in df.iterrows():
                # Check if the row contains at least one non-null value
                if not row.isnull().all():
                    # Initialize a flag to keep track of whether the column name is printed
                    printed_column_name = False
                    # Iterate through the columns
                    for idx, value in enumerate(row):
                        # Check if the value is not null
                        if pd.notnull(value):
                            # If the column has a name and it has not been printed yet, append the name
                            if df.columns[idx] != 'Unnamed: 0' and not printed_column_name:
                                text += df.columns[idx] + ": "
                                printed_column_name = True
                            # Append the value to the text
                            text += str(value) + " "
                    # Add a newline after processing each row
                    text += "\n"
    
    return text.strip()
