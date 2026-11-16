import pandas as pd
import numpy as np
import os

np.random.seed(42)

records = []

attack_types = ["Normal", "DDoS", "Brute Force", "Port Scan", "Botnet"]

for attack in attack_types:

    for i in range(2000):

        if attack == "Normal":
            duration = np.random.uniform(1, 10)
            packet_count = np.random.randint(10, 100)
            source_bytes = np.random.randint(500, 5000)
            destination_bytes = np.random.randint(500, 5000)
            failed_logins = np.random.randint(0, 2)
            connection_rate = np.random.uniform(1, 20)
            error_rate = np.random.uniform(0, 0.2)
            unusual_port_activity = 0

        elif attack == "DDoS":
            duration = np.random.uniform(0.1, 3)
            packet_count = np.random.randint(500, 2000)
            source_bytes = np.random.randint(5000, 20000)
            destination_bytes = np.random.randint(100, 2000)
            failed_logins = 0
            connection_rate = np.random.uniform(80, 100)
            error_rate = np.random.uniform(0.6, 1.0)
            unusual_port_activity = 0

        elif attack == "Brute Force":
            duration = np.random.uniform(5, 30)
            packet_count = np.random.randint(100, 500)
            source_bytes = np.random.randint(1000, 8000)
            destination_bytes = np.random.randint(500, 4000)
            failed_logins = np.random.randint(5, 30)
            connection_rate = np.random.uniform(20, 60)
            error_rate = np.random.uniform(0.2, 0.6)
            unusual_port_activity = 0

        elif attack == "Port Scan":
            duration = np.random.uniform(1, 15)
            packet_count = np.random.randint(100, 800)
            source_bytes = np.random.randint(500, 5000)
            destination_bytes = np.random.randint(100, 2000)
            failed_logins = 0
            connection_rate = np.random.uniform(40, 90)
            error_rate = np.random.uniform(0.3, 0.8)
            unusual_port_activity = 1

        else:  # Botnet
            duration = np.random.uniform(10, 60)
            packet_count = np.random.randint(200, 1000)
            source_bytes = np.random.randint(3000, 15000)
            destination_bytes = np.random.randint(2000, 10000)
            failed_logins = np.random.randint(0, 5)
            connection_rate = np.random.uniform(30, 80)
            error_rate = np.random.uniform(0.2, 0.7)
            unusual_port_activity = 1

        records.append([
            duration,
            packet_count,
            source_bytes,
            destination_bytes,
            failed_logins,
            connection_rate,
            error_rate,
            unusual_port_activity,
            attack
        ])

columns = [
    "duration",
    "packet_count",
    "source_bytes",
    "destination_bytes",
    "failed_logins",
    "connection_rate",
    "error_rate",
    "unusual_port_activity",
    "label"
]

df = pd.DataFrame(records, columns=columns)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Save dataset
df.to_csv("data/cyber_threat_dataset.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print("\nAttack distribution:")
print(df["label"].value_counts())