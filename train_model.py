import pandas as pd
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("data/cyber_threat_dataset.csv")

print("Dataset loaded successfully!")
print("Total records:", len(df))

# Input features
X = df.drop("label", axis=1)

# Target variable
y = df["label"]

# Split dataset: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# Create SVM Pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(
        kernel="rbf",
        C=1.0,
        gamma="scale",
        probability=True,
        random_state=42
    ))
])

# Train SVM model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nSVM Model Training Completed!")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Create models folder
os.makedirs("models", exist_ok=True)

# Save trained model
with open("models/threat_detection_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nSVM Model saved successfully!")
print("Location: models/threat_detection_model.pkl")
