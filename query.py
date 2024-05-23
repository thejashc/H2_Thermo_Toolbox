#!/opt/homebrew/bin/python3

import pandas as pd

def get_sheet_names(file_path):
    """
    Get all sheet names from the Excel file.

    :param file_path: Path to the Excel file.
    :return: List of sheet names.
    """
    try:
        excel_file = pd.ExcelFile(file_path)
        return excel_file.sheet_names
    except Exception as e:
        print(f"An error occurred while fetching sheet names: {e}")
        return []

def get_available_columns(file_path, sheet_name):
    """
    Get the available columns from the specified sheet in the Excel file.

    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet to read data from.
    :return: List of column names.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=0)  # Read only the header row
        return list(df.columns)
    except Exception as e:
        print(f"An error occurred while fetching columns: {e}")
        return []

def import_selected_columns(file_path, sheet_name, columns):
    """
    Import selected columns from an Excel sheet.

    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet to read data from.
    :param columns: List of columns to import.
    :return: DataFrame containing the selected columns.
    """
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns)
        return data
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
        return None

def export_data(data, file_name, file_format):
    """
    Export the DataFrame to the specified file format.

    :param data: DataFrame to be exported.
    :param file_name: Name of the output file.
    :param file_format: Format of the output file ('xlsx', 'csv', or 'dat').
    """
    try:
        if file_format == 'xlsx':
            data.to_excel(f"{file_name}.xlsx", index=False)
        elif file_format == 'csv':
            data.to_csv(f"{file_name}.csv", index=False)
        elif file_format == 'dat':
            data.to_csv(f"{file_name}.dat", index=False, sep='\t')
        print(f"Data exported successfully to {file_name}.{file_format}")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

def main():
    # Known file path
    file_path = "databank.xlsx"  # Change this to your file path

    # Get all sheet names
    sheet_names = get_sheet_names(file_path)

    if not sheet_names:
        print("No sheets found or unable to read the file.")
        return

    # Display available sheet names
    print("Available sheet names:")
    for idx, sheet in enumerate(sheet_names):
        print(f"{idx + 1}. {sheet}")

    # User input for sheet name
    while True:
        try:
            sheet_idx = int(input("Enter the number corresponding to the sheet name you want to use: ")) - 1
            if sheet_idx < 0 or sheet_idx >= len(sheet_names):
                print(f"Invalid selection. Please enter a number between 1 and {len(sheet_names)}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    sheet_name = sheet_names[sheet_idx]

    # Get available columns
    available_columns = get_available_columns(file_path, sheet_name)

    if not available_columns:
        print("No columns found or unable to read the sheet.")
        return

    print("Available columns:")
    for idx, col in enumerate(available_columns):
        print(f"{idx + 1}. {col}")

    # User input for columns to import
    while True:
        try:
            column_indices = input("Enter the numbers corresponding to the columns you want to import, separated by commas: ").split(',')
            column_indices = [int(idx.strip()) - 1 for idx in column_indices]
            if any(idx < 0 or idx >= len(available_columns) for idx in column_indices):
                print(f"Invalid selection. Please enter numbers between 1 and {len(available_columns)}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    columns = [available_columns[idx] for idx in column_indices]

    # Import the selected columns
    data = import_selected_columns(file_path, sheet_name, columns)

    # Display the imported data
    if data is not None:
        print("Imported Data:")
        print(data)
    else:
        print("Failed to import data.")
        return

    # User input for export format
    while True:
        export_format = input("Enter the export format (xlsx, csv, dat): ").strip().lower()
        if export_format in ['xlsx', 'csv', 'dat']:
            break
        else:
            print("Invalid format. Please enter 'xlsx', 'csv', or 'dat'.")

    # User input for export file name
    file_name = input("Enter the name for the output file (without extension): ").strip()

    # Export data
    export_data(data, file_name, export_format)

if __name__ == "__main__":
    main()

