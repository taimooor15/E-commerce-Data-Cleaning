import pandas as pd
import os

def clean_internship_data(input_file, output_file):
    print("Starting Data Integrity Audit:")
    
    # Check if the raw file exists
    if not os.path.exists(input_file):
        print(f"Error: Could not find '{input_file}' in the current folder.")
        print("Please ensure the Excel file is renamed exactly and placed here.")
        return

    # Load the dataset
    print("\nLoading raw dataset:")
    df = pd.read_excel(input_file)
    
    # Capture initial shape for reporting
    initial_rows, initial_cols = df.shape
    print(f"Initial Dataset Shape: {initial_rows} rows, {initial_cols} columns")
    
    print("\nStep 1: Handling Missing Values (Strategic Imputation):")
    coupon_cols = [col for col in df.columns if 'coupon' in col.lower()]
    if coupon_cols:
        for col in coupon_cols:
            df[col] = df[col].fillna("No coupon")
            print(f"Missing values in '{col}' filled with 'No coupon'.")
            
    for col in df.columns:
        if col in coupon_cols:
            continue
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("Unknown")
        elif df[col].dtype in ['int64', 'float64']:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)

    print("\nStep 2: Eliminating Duplicates:")
    before_dedup = len(df)
    df = df.drop_duplicates()
    after_dedup = len(df)
    print(f"Removed {before_dedup - after_dedup} exact duplicate rows.")

    print("\nStep 3: Formatting and Standardization:")
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
            df[col] = df[col].fillna("Unknown-Date")
            print(f"Standardized date column '{col}' to YYYY-MM-DD format.")
        except Exception as e:
            print(f"Could not format column '{col}' as date automatically: {e}")

    float_cols = df.select_dtypes(include=['float64']).columns
    for col in float_cols:
        df[col] = df[col].round(2)
        
    print("\nSaving clean 'Gold Standard' dataset")
    df.to_excel(output_file, index=False)
    
    print("\n" + "="*50)
    print("SUCCESS: DATA CLEANING COMPLETED!")
    print(f"Saved as: {output_file}")
    print(f"Final Cleaned Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("="*50)

if __name__ == "__main__":
    INPUT_DATASET = "data/Dataset for Data Analytics.xlsx"
    OUTPUT_DATASET = "data/Cleaned_Dataset.xlsx"
    clean_internship_data(INPUT_DATASET, OUTPUT_DATASET)