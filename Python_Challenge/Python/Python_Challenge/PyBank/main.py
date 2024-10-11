import pandas as pd

# Load the dataset from the CSV file
file_path = r"C:\Users\victo\OneDrive\文档\Python_Challenge\Python\Python_Challenge\PyBank\Resources\budget_data.csv" # This is where I saved my csv
data = pd.read_csv(file_path)

# Financial calculations
total_months = data['Date'].nunique()
net_total = data['Profit/Losses'].sum()
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()
greatest_increase = data.loc[data['Change'].idxmax()]
greatest_decrease = data.loc[data['Change'].idxmin()]

output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']:.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:.2f})\n"
)

# Print to terminal
print(output)

output_file_path = r"C:\Users\victo\OneDrive\文档\Python_Challenge\Python\Python_Challenge\PyBank\Analysis\financial_analysis_v2.txt" # This is where my text file is going to be 

try:
    with open(output_file_path, 'w') as file:
        file.write(output)
    print(f"Analysis exported to: {output_file_path}")
except Exception as e:
    print(f"Error occurred while writing the file: {e}")
