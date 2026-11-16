
import streamlit as st
import pandas as pd
import pickle


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)


# ==================================================
# RISK ASSESSMENT FUNCTION
# ==================================================

def calculate_risk(threat, confidence):

    if threat == "Normal":
        return "Low", 10

    severity = {
        "Port Scan": 50,
        "Brute Force": 65,
        "Botnet": 80,
        "DDoS": 90
    }

    base_score = severity.get(threat, 60)

    risk_score = (base_score * 0.7) + (confidence * 0.3)

    risk_score = min(round(risk_score), 100)

    if risk_score >= 85:
        level = "Critical"

    elif risk_score >= 70:
        level = "High"

    elif risk_score >= 40:
        level = "Medium"

    else:
        level = "Low"

    return level, risk_score


# ==================================================
# INTELLIGENT SECURITY ASSISTANT
# ==================================================

def display_security_assistant(threat):

    threat_information = {

        "Normal": {
            "explanation": (
                "The network activity appears normal. "
                "No suspicious behaviour was detected."
            ),

            "impact": (
                "No immediate security threat has been identified. "
                "Continue monitoring network activity."
            ),

            "actions": [
                "Continue routine network monitoring.",
                "Keep firewall and antivirus protection enabled.",
                "Maintain regular security updates.",
                "Monitor logs for unusual network behaviour."
            ]
        },

        "DDoS": {
            "explanation": (
                "A Distributed Denial of Service (DDoS) attack "
                "attempts to overwhelm a system or network "
                "with excessive traffic."
            ),

            "impact": (
                "It may cause service disruption, slow network "
                "performance or make the targeted service unavailable."
            ),

            "actions": [
                "Monitor and filter suspicious network traffic.",
                "Apply rate limiting to excessive requests.",
                "Block suspicious IP addresses when appropriate.",
                "Use firewall and DDoS protection mechanisms.",
                "Review network and server logs for unusual traffic."
            ]
        },

        "Brute Force": {
            "explanation": (
                "A Brute Force attack attempts to gain unauthorized "
                "access by repeatedly trying different passwords "
                "or login credentials."
            ),

            "impact": (
                "It may lead to unauthorized account access, "
                "credential theft or compromise of sensitive information."
            ),

            "actions": [
                "Enable multi-factor authentication (MFA).",
                "Implement account lockout policies.",
                "Use strong password requirements.",
                "Monitor repeated failed login attempts.",
                "Block suspicious login sources when appropriate."
            ]
        },

        "Port Scan": {
            "explanation": (
                "A Port Scan attack involves scanning network ports "
                "to identify open ports and discover available "
                "services on a target system."
            ),

            "impact": (
                "Attackers may identify vulnerable services and "
                "use them to plan further cyberattacks."
            ),

            "actions": [
                "Monitor unusual port scanning activity.",
                "Close unnecessary open ports.",
                "Configure firewall rules.",
                "Keep network services updated.",
                "Investigate suspicious source IP addresses."
            ]
        },

        "Botnet": {
            "explanation": (
                "A Botnet consists of compromised devices controlled "
                "remotely by an attacker to perform malicious activities."
            ),

            "impact": (
                "It may cause network disruption, data theft, "
                "unauthorized activities or participation in DDoS attacks."
            ),

            "actions": [
                "Identify and isolate compromised devices.",
                "Scan systems for malware.",
                "Monitor unusual outbound network traffic.",
                "Update operating systems and security software.",
                "Investigate suspicious communication patterns."
            ]
        }
    }

    information = threat_information[threat]

    st.divider()

    st.header("🤖 Intelligent Security Assistant")

    st.subheader("🔎 Threat Explanation")

    st.write(information["explanation"])

    st.subheader("⚠️ Possible Impact")

    st.write(information["impact"])

    st.subheader("🛡️ Recommended Security Actions")

    for action in information["actions"]:
        st.markdown(f"• {action}")


# ==================================================
# LOAD TRAINED SVM MODEL
# ==================================================

@st.cache_resource
def load_model():

    with open("models/threat_detection_model.pkl", "rb") as file:
        model = pickle.load(file)

    return model


model = load_model()


# ==================================================
# APPLICATION TITLE
# ==================================================

st.title("🛡️ AI Based Cyber Threat Detection")

st.subheader("Intelligent Security Assistant")

st.write(
    "Analyze network activity using Support Vector Machine (SVM) "
    "and detect potential cyber threats."
)

st.divider()


# ==================================================
# NETWORK ACTIVITY INPUT SECTION
# ==================================================

st.header("🔍 Network Activity Analysis")

col1, col2 = st.columns(2)


# LEFT SIDE INPUTS

with col1:

    duration = st.number_input(
        "Connection Duration (seconds)",
        min_value=0.0,
        value=2.0
    )

    packet_count = st.number_input(
        "Packet Count",
        min_value=0,
        value=50
    )

    source_bytes = st.number_input(
        "Source Bytes",
        min_value=0,
        value=1000
    )

    destination_bytes = st.number_input(
        "Destination Bytes",
        min_value=0,
        value=1000
    )


# RIGHT SIDE INPUTS

with col2:

    failed_logins = st.number_input(
        "Failed Login Attempts",
        min_value=0,
        value=0
    )

    connection_rate = st.slider(
        "Connection Rate",
        0.0,
        100.0,
        10.0
    )

    error_rate = st.slider(
        "Error Rate",
        0.0,
        1.0,
        0.1
    )

    unusual_port_activity = st.selectbox(
        "Unusual Port Activity",
        ["No", "Yes"]
    )


st.divider()


# ==================================================
# ANALYZE THREAT BUTTON
# ==================================================

if st.button(
    "🔎 Analyze Threat",
    use_container_width=True
):

    # Convert unusual port activity

    unusual_port = 1 if unusual_port_activity == "Yes" else 0


    # Prepare input data

    input_data = pd.DataFrame([{

        "duration": duration,

        "packet_count": packet_count,

        "source_bytes": source_bytes,

        "destination_bytes": destination_bytes,

        "failed_logins": failed_logins,

        "connection_rate": connection_rate,

        "error_rate": error_rate,

        "unusual_port_activity": unusual_port

    }])


    # ==================================================
    # SVM PREDICTION
    # ==================================================

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100


    # ==================================================
    # RISK CALCULATION
    # ==================================================

    risk_level, risk_score = calculate_risk(
        prediction,
        confidence
    )


    # ==================================================
    # DISPLAY ANALYSIS RESULT
    # ==================================================

    st.header("📊 Analysis Result")


    # NORMAL NETWORK ACTIVITY

    if prediction == "Normal":

        st.success(
            "✅ Network Activity is Normal"
        )

        result1, result2, result3 = st.columns(3)

        with result1:
            st.metric(
                "Activity",
                "Normal"
            )

        with result2:
            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        with result3:
            st.metric(
                "Risk Level",
                "Low"
            )


    # CYBER THREAT DETECTED

    else:

        st.error(
            "🚨 Cyber Threat Detected!"
        )

        result1, result2, result3, result4 = st.columns(4)

        with result1:
            st.metric(
                "Threat Type",
                prediction
            )

        with result2:
            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        with result3:
            st.metric(
                "Risk Level",
                risk_level
            )

        with result4:
            st.metric(
                "Risk Score",
                f"{risk_score}/100"
            )


        # Risk progress bar

        st.progress(
            risk_score / 100
        )


        # Risk warning

        if risk_level == "Critical":

            st.error(
                "🔴 Critical Risk — Immediate action recommended."
            )

        elif risk_level == "High":

            st.warning(
                "🟠 High Risk — Security investigation required."
            )

        elif risk_level == "Medium":

            st.warning(
                "🟡 Medium Risk — Monitor this activity."
            )

        else:

            st.info(
                "🟢 Low Risk"
            )


    # ==================================================
    # INTELLIGENT SECURITY ASSISTANT
    # ==================================================

    display_security_assistant(prediction)
