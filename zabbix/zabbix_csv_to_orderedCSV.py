import pandas as pd

# Replace 'input.csv' with your input CSV file path
input_file = 'input.csv'

# Replace 'output.csv' with your desired output CSV file path
output_file = 'output.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Select the desired columns
selected_columns = ['column1', 'column6', 'column10', 'column4', 'column8']

# Check if all selected columns exist in the DataFrame
if all(col in df.columns for col in selected_columns):
    # Order the DataFrame by the selected columns
    df = df[selected_columns].sort_values(by=['column1', 'column6', 'column10', 'column4', 'column8'])
    
    # Save the sorted DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f'Data sorted and saved to {output_file}')
else:
    print('One or more selected columns do not exist in the input CSV file.')