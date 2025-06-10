📦 Emotion Analyzer - README

This project builds a simple text emotion classifier using Python and machine learning. It processes a dataset of text samples labeled with emotions and trains a model that can predict the emotional tone of a new phrase.

📁 Folder Structure
emotion_analyzer/
├── app/
│ ├── predictor.py # Trains and saves model + vectorizer
│ ├── predict_text.py # Loads model and predicts emotion for a given phrase
│ ├── model.pkl # Saved Naive Bayes model (output)
│ ├── vectorizer.pkl # Saved TF-IDF vectorizer (output)
├── data/
│ ├── raw_dataset.csv # Original unfiltered dataset
│ ├── fixed_raw_dataset.csv # Cleaned version (malformed lines removed)
│ ├── dataset.csv # Processed text (normalized, cleaned)
│ ├── grouped_dataset.csv # Final dataset sorted by emotion (used for training)
├── scripts/
│ ├── fix_raw_dataset.py # Filters invalid rows from raw_dataset.csv
│ ├── clean_dataset.py # Cleans and normalizes text
│ ├── group_by_emotions.py # Sorts dataset by emotion
├── README.md # This file

⚙️ Scripts Overview

📂 app/predict_text.py
Purpose: Performs a prediction using the trained model and vectorizer.
Loads model.pkl and vectorizer.pkl
Vectorizes the input phrase
Prints the predicted emotion
Usage:
python app/predict_text.py

📂 app/predictor.py
Purpose: Trains a Naive Bayes classifier from the cleaned and grouped dataset.
Loads grouped_dataset.csv
Splits into training/test sets (80/20)
Applies TF-IDF vectorization
Trains and saves the model + vectorizer
Output:
model.pkl
vectorizer.pkl

📂 scripts/fix_raw_dataset.py
Purpose: Removes invalid lines from raw_dataset.csv
Retains only rows with exactly 2 columns
Discards malformed lines and logs a warning
Output:
fixed_raw_dataset.csv

📂 scripts/clean_dataset.py
Purpose: Cleans and normalizes the text.
Removes URLs and @mentions
Converts to lowercase
Normalizes whitespace
Output:
dataset.csv

📂 scripts/group_by_emotions.py
Purpose: Sorts the dataset by emotion.
Loads dataset.csv
Sorts rows by sentiment
Output:
grouped_dataset.csv

📚 Dataset Notes
raw_dataset.csv: Source data, possibly with formatting issues
fixed_raw_dataset.csv: Filtered rows, correct structure
dataset.csv: Cleaned text
✅ grouped_dataset.csv: Final version used for training (manually editable)
