import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Load processed datasets
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

X_train, y_train = train_df["title"] + " " + train_df["text"], train_df["label"]
X_test, y_test = test_df["title"] + " " + test_df["text"], test_df["label"]

# Build pipeline
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=300, class_weight='balanced')
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred, target_names=["FAKE", "REAL"]))

# Save model and vectorizer
joblib.dump(model, "models/fake_news_model.joblib")
joblib.dump(vectorizer, "models/tfidf_vectorizer.joblib")
print("Model and vectorizer saved!")
