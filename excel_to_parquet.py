import pandas as pd


def excel_to_parquet(excel_path, output_path='./output.parquet', exclude_sheets=None):
    """
    Converts all sheets (except those in exclude_sheets) in an Excel file into a single Parquet file.
    Assumes all included sheets have the same structure.
    
    Parameters:
        excel_path (str): Path to the Excel file.
        parquest_path (str): Path to the output Parquet file.
        exclude_sheets (list): List of sheet names to exclude.
    """
    exclude_sheets = exclude_sheets or []

    # Read all sheets
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    # Filter out excluded sheets
    included_sheets = {name: df for name, df in all_sheets.items() if name not in exclude_sheets}

    # Combine and export
    combined_df = pd.concat(included_sheets.values(), ignore_index=True)
    combined_df.to_parquet(output_path)
    print(f"Parquest file created at: {output_path}")