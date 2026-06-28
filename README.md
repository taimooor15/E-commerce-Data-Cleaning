# E-Commerce Data Analytics

A professional data analytics project focused on programmatic data cleaning, data preparation, and structural integrity auditing for e-commerce transactional data. 

This project takes a raw, unverified sales dataset and processes it into a reliable, analytical-ready "Gold Standard" dataset.

## Project Structure
The repository contains the following essential files:
* `Dataset for Data Analytics.xlsx` - The original, raw e-commerce dataset.
* `Cleaned_Dataset.xlsx` - The final, fully cleaned and standardized dataset.
* `python_code.ipynb` - The Python script containing the automated cleaning logic.

## Data Cleaning Steps Implemented
The Python pipeline automatically executes the following data integrity steps:
1. **Strategic Imputation:** Identifies missing values in critical columns and resolves them (e.g., filling empty cells in the coupon column with `'No coupon'`).
2. **Duplicate Elimination:** Audits the dataset for structural redundancies and removes exact duplicate rows to maintain data unique constraints.
3. **Format Standardization:** Uniformly formats structural elements, including standardizing the `Date` column to the `YYYY-MM-DD` format and stripping rogue whitespaces.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, OpenPyXL
* **Environment:** VS Code

