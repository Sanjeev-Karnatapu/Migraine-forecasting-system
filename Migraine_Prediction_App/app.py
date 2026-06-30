import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances
from pathlib import Path

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Migraine Severity Prediction System",
    page_icon="🧠",
    layout="wide"
)
st.title("🧠 AURANET")
st.subheader(
    "A Personalized Migraine Forecasting System with Multi-Feature Symptom Analysis"
)
# -------------------------------
# Load Dataset
# -------------------------------
import os

BASE_DIR = Path(__file__).parent

# st.write("Current working directory:", os.getcwd())
# st.write("Files in app folder:", os.listdir(BASE_DIR))

df = pd.read_csv(BASE_DIR / "slim enc mg.csv")
# -------------------------------
# User Configuration
# -------------------------------
st.header("👥 User Configuration")

num_users = st.number_input(
    "Enter the number of users to analyze:",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

selected_user = st.selectbox(
    "Select User to Enter Details",
    [f"User {i+1}" for i in range(num_users)]
)

user_idx = int(selected_user.split()[-1]) - 1

# -------------------------------
# Session Storage
# -------------------------------
if "users_data" not in st.session_state:
    st.session_state.users_data = [{} for _ in range(num_users)]

if len(st.session_state.users_data) != num_users:
    st.session_state.users_data = [{} for _ in range(num_users)]

st.info(f"Currently entering details for {selected_user}")
st.subheader(f"📝 Enter Details for {selected_user}")

user = st.session_state.users_data[user_idx]

# Numeric Inputs
user["Age"] = st.number_input(
    "Age (years)",
    min_value=1,
    max_value=100,
    value=user.get("Age", 25),
    key=f"age_{user_idx}"
)

user["Duration"] = st.number_input(
    "Typical migraine duration (hours)",
    min_value=0,
    max_value=72,
    value=user.get("Duration", 2),
    key=f"duration_{user_idx}"
)

user["Frequency"] = st.number_input(
    "Migraine attacks per week",
    min_value=0,
    max_value=20,
    value=user.get("Frequency", 1),
    key=f"freq_{user_idx}"
)

# Pain Location
location_options = {
    "One Side": 1,
    "Both Sides": 2,
    "Back of Head": 3
}

selected_location = st.selectbox(
    "Pain Location",
    list(location_options.keys()),
    key=f"location_{user_idx}"
)

user["Location"] = location_options[selected_location]


# Pain Type
character_options = {
    "Throbbing": 1,
    "Sharp / Stabbing": 2,
    "Dull / Pressure": 3
}

selected_character = st.selectbox(
    "Pain Type",
    list(character_options.keys()),
    key=f"character_{user_idx}"
)

user["Character"] = character_options[selected_character]

user["Intensity"] = st.slider(
    "Pain intensity",
    min_value=1,
    max_value=10,
    value=user.get("Intensity", 5),
    key=f"intensity_{user_idx}"
)

# Symptom Questions
questions = {
    "Nausea": "Nausea",
    "Vomit": "Vomiting",
    "Phonophobia": "Sensitivity to sound",
    "Photophobia": "Sensitivity to light",
    "Visual": "Visual aura",
    "Sensory": "Sensory symptoms",
    "Dysphasia": "Difficulty speaking",
    "Dysarthria": "Slurred speech",
    "Vertigo": "Vertigo",
    "Tinnitus": "Tinnitus",
    "Hypoacusis": "Reduced hearing",
    "Diplopia": "Double vision",
    "Defect": "Blind spots",
    "Ataxia": "Loss of coordination",
    "Conscience": "Confusion/loss of awareness",
    "Paresthesia": "Pins and needles",
    "DPF": "Post-migraine fatigue"
}

st.subheader("⚠️ Symptoms")

for col, label in questions.items():
    user[col] = 1 if st.checkbox(
        label,
        value=bool(user.get(col, 0)),
        key=f"{col}_{user_idx}"
    ) else 0

# Lifestyle Inputs
st.subheader("🌿 Lifestyle Information")

user["sleep_hours"] = st.slider(
    "Sleep hours per day",
    0.0,
    12.0,
    float(user.get("sleep_hours", 8.0)),
    0.5,
    key=f"sleep_{user_idx}"
)

user["physical_activity_minutes"] = st.number_input(
    "Physical activity (minutes/day)",
    min_value=0,
    value=user.get("physical_activity_minutes", 30),
    key=f"activity_{user_idx}"
)

user["sunlight_exposure_minutes"] = st.number_input(
    "Sunlight exposure (minutes/day)",
    min_value=0,
    value=user.get("sunlight_exposure_minutes", 20),
    key=f"sunlight_{user_idx}"
)

user["hydration_liters"] = st.number_input(
    "Water intake (liters/day)",
    min_value=0.0,
    value=float(user.get("hydration_liters", 2.0)),
    step=0.1,
    key=f"water_{user_idx}"
)

# Save user data
st.session_state.users_data[user_idx] = user

st.success(f"✅ Details saved for {selected_user}")
st.divider()
def lifestyle_suggestions(user, severity):
    suggestions = []

    if severity == "🟢 Normal":
        suggestions.append(
            "✅ Maintain your healthy lifestyle."
        )

    elif severity == "🟡 Medium":
        if user["sleep_hours"] < 7:
            suggestions.append(
                "💤 Increase sleep to 7-8 hours."
            )

        if user["hydration_liters"] < 2:
            suggestions.append(
                "💧 Drink at least 2 liters of water daily."
            )

        if user["physical_activity_minutes"] < 30:
            suggestions.append(
                "🏃 Exercise for at least 30 minutes daily."
            )

        if user["sunlight_exposure_minutes"] < 15:
            suggestions.append(
                "☀️ Spend more time in natural sunlight."
            )

        suggestions.append(
            "📱 Reduce screen exposure."
        )

        suggestions.append(
            "📝 Maintain a migraine diary."
        )

    else:
        suggestions.append(
            "🚨 Severe migraine risk detected."
        )

        if user["sleep_hours"] < 7:
            suggestions.append(
                "💤 Increase sleep duration."
            )

        if user["hydration_liters"] < 2:
            suggestions.append(
                "💧 Increase water intake to 2-3 liters."
            )

        if user["physical_activity_minutes"] < 30:
            suggestions.append(
                "🏃 Increase physical activity."
            )

        if user["sunlight_exposure_minutes"] < 15:
            suggestions.append(
                "☀️ Increase sunlight exposure."
            )

        if user["Frequency"] >= 4:
            suggestions.append(
                "🩺 Consult a neurologist due to frequent attacks."
            )

        if user["Intensity"] >= 8:
            suggestions.append(
                "⚠️ Medical supervision is recommended."
            )

        suggestions.append(
            "🥗 Eat foods rich in magnesium and omega-3."
        )

        suggestions.append(
            "🧘 Practice stress-management techniques."
        )

        suggestions.append(
            "📱 Reduce prolonged screen exposure."
        )

        suggestions.append(
            "📝 Maintain a migraine trigger diary."
        )

    return suggestions
if st.button("🧠 Predict Migraine Severity"):

    users_data = st.session_state.users_data

    # Model coefficients
    b0, b1, b2, b3, b4, b5, b6 = (
        0.2, 0.1, 0.15, 0.25, 0.05, 0.2, 0.15
    )

    a0 = 0.1
    a = [
        0.1, 0.1, 0.1, 0.1,
        0.15, 0.1, 0.1, 0.05,
        0.1, 0.1, 0.1, 0.1
    ]

    c0, c1, c2, c3, c4 = (
        0.3, 0.5, 0.4, 0.01, 0.2
    )

    aura_symptoms = [
        "Visual", "Sensory", "Dysphasia",
        "Dysarthria", "Vertigo", "Tinnitus",
        "Hypoacusis", "Diplopia", "Defect",
        "Ataxia", "Conscience", "Paresthesia"
    ]

    st.header("📊 Prediction Results")
    
    actual_mss_list = []
    predicted_mss_list = []
    
    actual_ass_list = []
    predicted_ass_list = []
    
    actual_osi_list = []
    predicted_osi_list = []
    for idx, user in enumerate(users_data):

        # Skip incomplete users
        if len(user) == 0:
            continue

        MSS = (
            b0
            + b1 * user["Duration"]
            + b2 * user["Frequency"]
            + b3 * user["Nausea"]
            + b4 * user["Vomit"]
            + b5 * user["Phonophobia"]
            + b6 * user["Photophobia"]
        )

        ASS = a0 + sum(
            a[i] * user[aura_symptoms[i]]
            for i in range(len(aura_symptoms))
        )

        OSI = (
            c0
            + c1 * MSS
            + c2 * ASS
            + c3 * user["Age"]
            + c4 * user["Frequency"]
        )

        # Save results
        user["MSS"] = MSS
        user["ASS"] = ASS
        user["OSI"] = OSI
        # -------------------------------
        # Find nearest dataset match
        # -------------------------------
        
        symptom_cols = [
            "Age","Duration","Frequency","Location","Character","Intensity",
            "Nausea","Vomit","Phonophobia","Photophobia","Visual","Sensory",
            "Dysphasia","Dysarthria","Vertigo","Tinnitus","Hypoacusis",
            "Diplopia","Defect","Ataxia","Conscience","Paresthesia","DPF",
            "sleep_hours","physical_activity_minutes",
            "sunlight_exposure_minutes","hydration_liters"
        ]
        
        user_row = pd.DataFrame([user])[symptom_cols]
        matching_row = df[symptom_cols]
        
        distances = pairwise_distances(
            matching_row,
            user_row
        )
        
        nearest_idx = np.argmin(distances)
        
        actual_MSS = df.loc[
            nearest_idx,
            "Migraine_Severity_Score"
        ]
        
        actual_ASS = df.loc[
            nearest_idx,
            "Aura_Severity_Score"
        ]
        
        actual_OSI = df.loc[
            nearest_idx,
            "Overall_Severity_Index"
        ]
        
        user["Actual_MSS"] = actual_MSS
        user["Actual_ASS"] = actual_ASS
        user["Actual_OSI"] = actual_OSI
        actual_mss_list.append(actual_MSS)
        predicted_mss_list.append(MSS)
        
        actual_ass_list.append(actual_ASS)
        predicted_ass_list.append(ASS)
        
        actual_osi_list.append(actual_OSI)
        predicted_osi_list.append(OSI)
        # Severity
        if OSI < 1.5:
            severity = "🟢 Normal"
        elif OSI < 2.5:
            severity = "🟡 Medium"
        else:
            severity = "🔴 Severe"

        st.subheader(f"👤 User {idx+1}")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Migraine Severity Score (MSS)",
            f"{MSS:.2f}"
        )

        col2.metric(
            "Aura Severity Score (ASS)",
            f"{ASS:.2f}"
        )

        col3.metric(
            "Overall Severity Index (OSI)",
            f"{OSI:.2f}"
        )

        st.success(f"Predicted Severity: {severity}")
        dataset_col1, dataset_col2, dataset_col3 = st.columns(3)
        
        dataset_col1.metric(
            "Dataset MSS",
            f"{actual_MSS:.2f}",
            delta=f"{MSS - actual_MSS:.2f}"
        )
        
        dataset_col2.metric(
            "Dataset ASS",
            f"{actual_ASS:.2f}",
            delta=f"{ASS - actual_ASS:.2f}"
        )
        
        dataset_col3.metric(
            "Dataset OSI",
            f"{actual_OSI:.2f}",
            delta=f"{OSI - actual_OSI:.2f}"
        )
        
        # ==========================
        # Lifestyle Recommendations
        # ==========================
        st.subheader(f"🧾 Lifestyle Recommendations for User {idx+1}")
        
        recommendations = lifestyle_suggestions(
            user,
            severity
        )
        
        for rec in recommendations:
            st.write(rec)
        
        st.divider()
        
    st.header("📈 Overall Comparison Graphs")
        
    users = [f"User {i+1}" for i in range(len(predicted_mss_list))]
        
    # ==========================
    # MSS Graph
    # ==========================
    fig1, ax1 = plt.subplots(figsize=(5, 2.5))
        
    ax1.plot(
        users,
        actual_mss_list,
        marker="o",
        linewidth=2,
        label="Actual MSS"
    )
        
    ax1.plot(
        users,
        predicted_mss_list,
        marker="s",
        linewidth=2,
        linestyle="--",
        label="Predicted MSS"
    )
        
    ax1.set_title("Actual vs Predicted Migraine Severity Score (MSS)")
    ax1.set_xlabel("Users")
    ax1.set_ylabel("MSS")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
        
    st.pyplot(fig1, use_container_width=False)
        
    # ==========================
    # ASS Graph
    # ==========================
    fig2, ax2 = plt.subplots(figsize=(5, 2.5))
        
    ax2.plot(
        users,
        actual_ass_list,
        marker="o",
        linewidth=2,
        label="Actual ASS"
    )
    ax2.plot(
        users,
        predicted_ass_list,
        marker="s",
        linewidth=2,
        linestyle="--",
        label="Predicted ASS"
    )
        
    ax2.set_title("Actual vs Predicted Aura Severity Score (ASS)")
    ax2.set_xlabel("Users")
    ax2.set_ylabel("ASS")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
        
    st.pyplot(fig2, use_container_width=False)
        
    # ==========================
    # OSI Graph
    # ==========================
    fig3, ax3 = plt.subplots(figsize=(5, 2.5))
        
    ax3.plot(
        users,
        actual_osi_list,
        marker="o",
        linewidth=2,
        label="Actual OSI"
    )
        
    ax3.plot(
        users,
        predicted_osi_list,
        marker="s",
        linewidth=2,
        linestyle="--",
        label="Predicted OSI"
    )
        
    ax3.set_title("Actual vs Predicted Overall Severity Index (OSI)")
    ax3.set_xlabel("Users")
    ax3.set_ylabel("OSI")
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    st.pyplot(fig3, use_container_width=False)
