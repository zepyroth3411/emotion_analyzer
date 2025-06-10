from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

trained_model = joblib.load('model.pkl')
loaded_vectorizer = joblib.load('vectorizer.pkl')

texto = ['I feel happy today']

# Vectorize using the pre-trained vectorizer
vectorized_input = loaded_vectorizer.transform(texto)



# Predict
prediction = trained_model.predict(vectorized_input)
print(prediction[0])  # e.g., "sadness"
