# Retail Sales Analysis

A Python script for exploring the Sample Superstore retail dataset. It reports
data quality checks and business metrics, compares product and regional
performance, and creates a chart of profit by product category.

## Project files

```text
retail-sales-analysis/
├── retail_analysis.py
├── data/
│   ├── Sample - Superstore.csv
│   └── requirements.txt
└── README.md
```

The script expects the CSV at `data/Sample - Superstore.csv`, relative to the
project directory. It reads the file using the `cp1252` encoding.

## Requirements

- Python 3
- Packages listed in `data/requirements.txt` (`pandas`, `numpy`,
  `matplotlib`, `seaborn`, `jupyter`, and `ipykernel`)

## Setup and run (Windows PowerShell)

From the project directory, install the dependencies and run the script:

```powershell
python -m pip install -r .\data\requirements.txt
python .\retail_analysis.py
```

The script uses `Path(__file__).resolve().parent` to locate the project
directory, so the input CSV path does not depend on the shell's current
directory. The chart is saved as `profit_by_category.png` in the current
working directory and also displayed in a plot window.

## Analysis steps and methods

1. **Load the data** – Read the CSV into a pandas DataFrame, then print its
   dimensions, first five rows, and column names. 'df = pd.read_csv'
2. **Inspect the data** – Use `DataFrame.info()` and `DataFrame.describe()` to
   review column types and descriptive statistics. Count missing values and
   exact duplicate rows.
3. **Prepare a clean working copy** – Copy the original DataFrame. Convert
   `Order Date` and `Ship Date` to datetimes with invalid values coerced to
   `NaT`, and treat `Postal Code` as a string identifier rather than a number.
   Print invalid date counts, updated types, and validation checks. The script
   does not remove rows or impute missing values.
4. **Calculate overall metrics** – Sum sales, profit, and quantity; count
   distinct orders and customers; calculate average sales per order as total
   sales divided by distinct orders; and calculate overall profit margin as
   profit divided by sales, multiplied by 100.
5. **Compare product categories** – Group rows by `Category`, aggregate total
   sales, total profit, and units sold, calculate each category's profit
   margin, and sort by sales in descending order.
6. **Compare sub-categories** – Group by `Sub-Category`, aggregate sales,
   profit, and units, then print the five highest- and lowest-profit
   sub-categories.
7. **Compare regions** – Group by `Region`, aggregate sales and profit, count
   distinct orders, and sort by profit in descending order.
8. **Visualize category profit** – Use Seaborn's bar plot to chart total profit
   by category, add labels and a title, apply a tight layout, and save the
   image at 300 DPI.

## Output

The console displays dataset inspection and validation results, overall
business metrics, and the category, sub-category, and regional summaries. The
chart is saved as `profit_by_category.png`.
