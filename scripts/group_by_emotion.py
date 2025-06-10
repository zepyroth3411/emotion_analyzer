import pandas as pd
import os

# === PATHS ===
script_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(script_path))
dataset_path = os.path.join(project_path, 'data', 'dataset.csv')
output_path = os.path.join(project_path, 'data', 'grouped_dataset.csv')

# === LOAD CSV ===
df = pd.read_csv(dataset_path)

# === ORDER BY EMOTION ===
df_sorted = df.sort_values(by='sentiment')

# === SAVE NEW FILE ===
df_sorted.to_csv(output_path, index=False)
print(f"Grouped dataset saved to: {output_path}")