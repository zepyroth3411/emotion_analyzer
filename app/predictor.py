import os 
import pandas as pd 
from sklearn.model_selection import train_test_split

# === PATHS ===
script_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(script_path))
clean_csv_path = os.path.join(project_path, 'data', 'dataset.csv')

# === LOAD AND CLEAN DATA ===
df = pd.read_csv(clean_csv_path)
print(df)

#entrenamiento

X = df['content']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




# === SAVE CLEANED CSV ===
#df.to_csv(clean_csv_path, index=False)
