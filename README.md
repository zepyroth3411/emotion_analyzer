# emotion_analyzer

📄 clean_dataset.py
This script performs data cleaning on the raw tweet emotion dataset. It:
Loads the raw CSV file from the data/ directory.
Drops unnecessary columns, such as tweet_id.
Cleans the tweet content by:
Removing URLs.
Removing user mentions (e.g., @username).
Converting text to lowercase.
Replacing multiple spaces with a single space.
Stripping leading and trailing whitespace.
Saves the cleaned dataset to data/dataset.csv.
This cleaned file will be used for training a simple emotion classifier later in the project.