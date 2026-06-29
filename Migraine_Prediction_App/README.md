# 🧠 Migraine Forecasting System

A Python-based healthcare analytics project that predicts migraine severity using patient symptoms, aura indicators, and lifestyle factors. The system calculates severity scores, compares user profiles with historical migraine data, visualizes results, and provides personalized lifestyle recommendations.

## 🚀 Features

### 📋 Patient Data Collection
- Age
- Migraine duration
- Weekly attack frequency
- Pain location
- Pain type
- Pain intensity

### 🩺 Symptom Assessment
- Nausea
- Vomiting
- Photophobia (light sensitivity)
- Phonophobia (sound sensitivity)

### 🌈 Aura Symptom Analysis
- Visual disturbances
- Sensory abnormalities
- Dysphasia
- Dysarthria
- Vertigo
- Tinnitus
- Hypoacusis
- Diplopia
- Visual defects
- Ataxia
- Altered consciousness
- Paresthesia

### 🏃 Lifestyle Analysis
- Sleep duration
- Physical activity
- Sunlight exposure
- Daily hydration

### 📊 Severity Prediction
- Migraine Severity Score (MSS)
- Aura Severity Score (ASS)
- Overall Severity Index (OSI)

### 🔍 Dataset Matching
- Exact record matching
- Nearest-neighbor similarity matching

### 📈 Data Visualization
- MSS comparison graphs
- ASS comparison graphs
- OSI comparison graphs
- Prediction analysis plots

### 💡 Personalized Recommendations
- Sleep improvement guidance
- Hydration recommendations
- Physical activity suggestions
- Stress management advice
- Severe migraine alerts

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

## 📂 Project Structure

```text
Migraine-forecasting-system/
│
├── migraine model.ipynb
├── slim enc mg.csv
├── README.md
│
├── .ipynb_checkpoints/
└── .virtual_documents/
```

## ⚙️ How It Works

1. Load the migraine dataset.
2. Collect patient symptom and lifestyle information.
3. Calculate MSS, ASS, and OSI scores.
4. Compare the patient profile with historical dataset records.
5. Classify migraine severity.
6. Generate visual analytics.
7. Provide personalized lifestyle recommendations.

## ⚠️ Severity Classification

| OSI Range | Severity |
|-----------|-----------|
| < 1.5 | Normal |
| 1.5 - 2.5 | Medium |
| > 2.5 | Severe |

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Sanjeev-Karnatapu/Migraine-forecasting-system.git
cd Migraine-forecasting-system
```

Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## ▶️ Run the Project

For Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
migraine model.ipynb
```

## 📊 Output

The system provides:

- Migraine Severity Score (MSS)
- Aura Severity Score (ASS)
- Overall Severity Index (OSI)
- Severity Classification
- Dataset Similarity Analysis
- Personalized Lifestyle Recommendations
- Graphical Visualizations

## 🔮 Future Enhancements

- Machine Learning-based severity prediction
- Streamlit web application
- Migraine risk forecasting
- PDF report generation
- Real-time monitoring dashboard
- Wearable device integration

## 🎯 Applications

- Migraine severity assessment
- Healthcare decision support
- Patient self-monitoring
- Lifestyle risk analysis
- Medical research assistance

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. It is not a substitute for professional medical diagnosis or treatment. Always consult a qualified healthcare professional regarding migraine-related concerns.

## 👨‍💻 Author

**Sanjeev Karnatapu**

Computer Science Engineering | Artificial Intelligence and Machine Learning | VIT Vellore