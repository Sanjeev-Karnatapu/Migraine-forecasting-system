\# 🧠 Migraine Severity Detection and Lifestyle Recommendation System



A Python-based healthcare analytics project that predicts \*\*Migraine Severity\*\*, \*\*Aura Severity\*\*, and \*\*Overall Severity Index (OSI)\*\* using patient symptoms, migraine characteristics, and lifestyle factors. The system compares user inputs with a migraine dataset, classifies severity levels, visualizes results, and provides personalized lifestyle recommendations.



\---



\## 📌 Project Overview



Migraines affect millions of people worldwide and can significantly impact daily life. This project aims to assist in migraine assessment by:



\- Collecting patient symptom data interactively.

\- Computing severity scores using predefined clinical-weight formulas.

\- Comparing user profiles with historical migraine records.

\- Classifying migraine severity into Normal, Medium, or Severe.

\- Generating visual analysis plots.

\- Providing lifestyle improvement recommendations.



\---



\## 🚀 Features



\### 👤 User Data Collection

Captures:

\- Age

\- Migraine duration

\- Weekly attack frequency

\- Pain location

\- Pain type/character

\- Pain intensity



\### 🩺 Symptom Assessment

Evaluates:

\- Nausea

\- Vomiting

\- Photophobia (light sensitivity)

\- Phonophobia (sound sensitivity)



\### 🌈 Aura Symptom Detection

Analyzes:

\- Visual disturbances

\- Sensory abnormalities

\- Dysphasia

\- Dysarthria

\- Vertigo

\- Tinnitus

\- Hypoacusis

\- Diplopia

\- Visual defects

\- Ataxia

\- Altered consciousness

\- Paresthesia



\### 🏃 Lifestyle Analysis

Includes:

\- Sleep duration

\- Physical activity

\- Sunlight exposure

\- Daily hydration



\### 📊 Severity Prediction

Computes:

\- \*\*Migraine Severity Score (MSS)\*\*

\- \*\*Aura Severity Score (ASS)\*\*

\- \*\*Overall Severity Index (OSI)\*\*



\### 🔍 Dataset Matching

\- Exact patient profile matching

\- Nearest-neighbor similarity matching when no exact match exists



\### 📈 Visualization

Generates:

\- MSS comparison plots

\- ASS comparison plots

\- OSI comparison plots

\- Prediction performance scatter plots



\### 💡 Personalized Recommendations

Provides:

\- Sleep improvement suggestions

\- Hydration recommendations

\- Physical activity guidance

\- Stress management advice

\- Neurological consultation alerts for severe cases



\---



\## 🏗️ System Workflow



1\. Load migraine dataset

2\. Collect patient information

3\. Calculate MSS, ASS, and OSI scores

4\. Compare with historical dataset records

5\. Classify migraine severity

6\. Generate visual analytics

7\. Provide personalized lifestyle recommendations



\---



\## 📂 Dataset Requirements



The dataset (`slim enc mg.csv`) should contain features such as:



| Category | Attributes |

|-----------|------------|

| Demographics | Age |

| Migraine Characteristics | Duration, Frequency, Location, Character, Intensity |

| Symptoms | Nausea, Vomit, Photophobia, Phonophobia |

| Aura Symptoms | Visual, Sensory, Dysphasia, Vertigo, etc. |

| Lifestyle Factors | Sleep Hours, Physical Activity, Sunlight Exposure, Hydration |

| Target Variable | Overall\_Severity\_Index |



\---



\## 🧮 Severity Scoring Methodology



\### Migraine Severity Score (MSS)

Calculated using:

\- Attack duration

\- Attack frequency

\- Nausea

\- Vomiting

\- Sound sensitivity

\- Light sensitivity



\### Aura Severity Score (ASS)

Calculated from:

\- Visual aura symptoms

\- Sensory aura symptoms

\- Speech disturbances

\- Vestibular symptoms

\- Other neurological manifestations



\### Overall Severity Index (OSI)

A weighted combination of:

\- MSS

\- ASS

\- Age

\- Migraine frequency



\---



\## ⚠️ Severity Classification



| OSI Range | Classification |

|------------|---------------|

| < 1.5 | Normal |

| 1.5 – 2.5 | Medium |

| > 2.5 | Severe |



\---



\## 📊 Output Examples



\### Predicted Severity

```

User 1 Analysis



Predicted OSI: 2.87 → Severe

Dataset OSI: 2.75 → Severe

```



\### Lifestyle Recommendations

```

🚨 Severe migraine risk detected



✔ Consult a neurologist

✔ Maintain 7–8 hours of sleep

✔ Drink 2–3 liters of water daily

✔ Reduce screen exposure

✔ Manage stress through meditation

✔ Track migraine triggers regularly

```



\---



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Scikit-learn



\---



\## 📦 Installation



\### Clone Repository



```bash

git clone https://github.com/your-username/migraine-severity-detection.git

cd migraine-severity-detection

```



\### Install Dependencies



```bash

pip install pandas numpy matplotlib scikit-learn

```



\### Run Project



```bash

python migraine\_detection.py

```



\---



\## 📈 Future Enhancements



\- Machine Learning-based severity prediction

\- Streamlit web application

\- Real-time migraine monitoring dashboard

\- Personalized trigger detection

\- PDF report generation

\- Integration with wearable health devices



\---



\## 🎯 Applications



\- Migraine severity assessment

\- Healthcare decision support

\- Patient self-monitoring

\- Lifestyle risk analysis

\- Neurological research assistance



\---



\## ⚠️ Disclaimer



This project is intended for educational and research purposes only. It is not a substitute for professional medical diagnosis, treatment, or advice. Always consult a qualified healthcare provider regarding migraine-related concerns.



\---



\## 👨‍💻 Author



\*\*Sanjeev Karnatapu\*\*



Developed as a healthcare analytics project for migraine severity assessment and lifestyle recommendation using Python and data-driven techniques.

