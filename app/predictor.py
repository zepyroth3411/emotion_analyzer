import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# === Define useful paths ===
# Get the current script's absolute path
script_path = os.path.abspath(__file__)
# Get the project's root directory (one level up from /app)
project_path = os.path.dirname(os.path.dirname(script_path))
# Path to the cleaned dataset CSV file
clean_csv_path = os.path.join(project_path, 'data', 'dataset.csv')

# === Load the dataset ===
df = pd.read_csv(clean_csv_path)

# Split dataset into features (text) and labels (emotions)
X = df['content']        # input text
y = df['sentiment']      # target labels (emotions)

# Split data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === Text vectorization ===
# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
x_train_vect = vectorizer.fit_transform(X_train)

# === Train a classifier ===
# Use Naive Bayes (good baseline for text classification)
modelo = MultinomialNB()
modelo.fit(x_train_vect, y_train)

# === Save model and vectorizer ===
# Save the trained model and vectorizer to .pkl files for reuse
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(modelo, 'model.pkl')