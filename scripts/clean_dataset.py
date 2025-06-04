import os
import pandas as pd

def clean_text(dataframe):
    # Remove URLs
    dataframe['content'] = dataframe['content'].str.replace(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        ' ',
        regex=True
    )
    # Remove mentions like @username
    dataframe['content'] = dataframe['content'].str.replace(r'@\w+', '', regex=True)
    
    # Convert text to lowercase
    dataframe['content'] = dataframe['content'].str.lower()
    
    # Replace multiple spaces with a single space
    dataframe['content'] = dataframe['content'].str.replace(r'\s+', ' ', regex=True)
    
    # Strip leading/trailing whitespace
    dataframe['content'] = dataframe['content'].str.strip()
    return dataframe

# === PATHS ===
script_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(script_path))

raw_csv_path = os.path.join(project_path, 'data', 'raw_dataset.csv')
clean_csv_path = os.path.join(project_path, 'data', 'dataset.csv')

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(clean_csv_path), exist_ok=True)

# === LOAD AND CLEAN DATA ===
df = pd.read_csv(raw_csv_path)
df.drop("tweet_id", axis=1, inplace=True)
df = clean_text(df)

# === SAVE CLEANED CSV ===
df.to_csv(clean_csv_path, index=False)
