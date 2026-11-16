import pickle
import pandas as pd

# Load trained SVM model
with open("models/threat_detection_model.pkl", "rb") as file:
    model = pickle.load(file)

# Sample network activity
sample = pd.DataFrame([{
    "duration": 1.2,
    "packet_count": 1500,
    "source_bytes": 12000,
    "destination_bytes": 800,
    "failed_logins": 0,
    "connection_rate": 95,
    "error_rate": 0.85,
    "unusual_port_activity": 0
}])

# Predict threat
prediction = model.predict(sample)[0]

# Prediction probability
probabilities = model.predict_proba(sample)[0]
confidence = max(probabilities) * 100

print("AI Cyber Threat Detection - SVM")
print("--------------------------------")

print("Predicted Activity:", prediction)
print("Confidence:", round(confidence, 2), "%")

if prediction == "Normal":
    print("Status: Safe")
else:
    print("Status: Threat Detected!")
