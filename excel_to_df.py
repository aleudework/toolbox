import pandas as pd

def excel_to_df(excel_path, exclude_sheets=None):
    """
    Reads all sheets in an Excel file, excluding specified ones, and returns them as one combined DataFrame.

    Parameters:
        excel_path (str): Path to the Excel file.
        exclude_sheets (list): List of sheet names to exclude (optional).
    """
    exclude_sheets = exclude_sheets or []

    # Read all sheets into a dict of DataFrames
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    # Filter out excluded sheets
    included_sheets = {name: df for name, df in all_sheets.items() if name not in exclude_sheets}

    # Combine and return as one DataFrame
    return pd.concat(included_sheets.values(), ignore_index=True)