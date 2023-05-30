import pandas as pd

df = pd.read_csv('Awarding_data.csv')

# Iterate over each column in the DataFrame
for column in df.columns:
    # Filter values exceeding the varchar(255) limit
    exceeding_values = df[df[column].astype(str).str.len() > 255][column]

    # Print the exceeding values
    if not exceeding_values.empty:
        print(f"Exceeding values in column '{column}':")
        for value in exceeding_values:
            print(value)
        print()