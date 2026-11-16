# AI-Based Cyber Threat Detection and Intelligent Security Assistant 🛡️

## About the Project

Cybersecurity is becoming increasingly important as more activities move online. Different types of attacks can affect systems and networks, so identifying suspicious activity at an early stage is important.

I developed this project to detect different types of cyber threats using machine learning. It uses a Support Vector Machine (SVM) model to analyze network activity and predict whether it is normal or potentially harmful.

Along with threat detection, the project also includes an Intelligent Security Assistant that explains the detected threat, describes its possible impact, and suggests some steps that can be taken to improve security.

## What Does It Do?

The application takes network activity details as input and uses the trained model to classify the activity.

It can identify the following five categories:

- **Normal:** Regular network activity.
- **DDoS:** Excessive traffic that may disrupt a network or service.
- **Brute Force:** Repeated attempts to access an account using different passwords.
- **Port Scan:** Scanning ports to find open services on a system.
- **Botnet:** A group of compromised devices controlled by an attacker.

After making a prediction, the application displays the confidence score and risk level. If a threat is detected, the security assistant also provides an explanation and recommended actions.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Support Vector Machine (SVM)
- StandardScaler
- Streamlit
- Pickle

## Dataset

For this project, I generated a synthetic dataset using Python, Pandas, and NumPy.

It contains 10,000 records divided equally among the five categories, with 2,000 records for each category.

The dataset includes eight features:

1. Duration
2. Packet Count
3. Source Bytes
4. Destination Bytes
5. Failed Logins
6. Connection Rate
7. Error Rate
8. Unusual Port Activity

The dataset is stored in CSV format and is used to train and test the machine learning model.

*Note: This is a synthetically generated dataset created for learning and project development. It is not collected from actual network traffic.*

## Machine Learning Model

I used the Support Vector Machine (SVM) algorithm with an RBF kernel for multi-class threat classification.

The dataset is divided into training and testing sets in an 80:20 ratio. StandardScaler is used for feature scaling before training the model.

After training, the model is evaluated using accuracy and a classification report. The trained model is then saved as a Pickle file for use in the application.

## Project Structure

```text
Cyber_Threat_Detection/
│
├── data/
│   └── cyber_threat_dataset.csv
│
├── models/
│   └── threat_detection_model.pkl
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   └── test_model.py
│
├── assets/
├── app.py
├── requirements.txt
└── README.md
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/AI-Based-Cyber-Threat-Detection-and-Intelligent-Security-Assistant.git
```

**2. Open the project folder**

```bash
cd AI-Based-Cyber-Threat-Detection-and-Intelligent-Security-Assistant
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Generate the dataset**

```bash
python src/generate_dataset.py
```

**5. Train the model**

```bash
python src/train_model.py
```

**6. Test the model**

```bash
python src/test_model.py
```

**7. Start the application**

```bash
streamlit run app.py
```

## Application Features

- Enter network activity details manually.
- Detect and classify possible cyber threats.
- View prediction confidence.
- Check the calculated risk score and risk level.
- Understand the detected threat through the security assistant.
- Get recommended security actions based on the prediction.

## Future Improvements

Some things I would like to explore further in this project include:

- Using real-world network traffic datasets.
- Adding real-time network activity monitoring.
- Improving threat detection accuracy.
- Adding more threat categories.
- Exploring AI-based security analysis and automated alerts.

## Author

**Aishwarya Sharma**

B.Tech – Computer Science and Engineering

---

*This project was developed as part of my academic work to explore machine learning applications in cybersecurity.*
