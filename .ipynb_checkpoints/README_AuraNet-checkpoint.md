# AuraNet: Personalized Migraine Forecasting System
### A Hybrid Machine Learning Framework for Multi-Feature Symptom Analysis

---

## Overview
AuraNet is a Python-based intelligent healthcare system that forecasts migraine severity using multi-feature symptom and lifestyle analysis.  
It combines Machine Learning (LightGBM, CATBoost) and Deep Learning (TabPFN) concepts, along with engineered clinical indices —  
Migraine Severity Score (MSS), Aura Severity Score (ASS), and Overall Severity Index (OSI)— to deliver accurate, personalized predictions and actionable lifestyle recommendations.

---

##  Features
✅ Predicts migraine severity levels (*Normal*, *Medium*, *Severe*)  
✅ Performs hybrid multi-feature symptom analysis  
✅ Handles class imbalance via **SMOTE**  
✅ Computes derived health indices (MSS, ASS, OSI)  
✅ Provides personalized lifestyle recommendations  
✅ Visualizes **Actual vs Predicted** values and comparison plots  
✅ Implements patient-level analysis with interactive input  

---

## Tech Stack
| Component  | Description |
|------------|-------------|
| **Language** | Python 3.x |
| **Libraries** | Pandas, NumPy, Matplotlib, Scikit-learn |
| **Algorithms** | CATBoost, LightGBM, TabPFN |
| **Tools** | TensorFlow, PyTorch (for deep learning extensions) |
| **Visualization** | Matplotlib, Seaborn |

---
## Execution - Instructions

Install required libraries:

pip install pandas numpy matplotlib scikit-learn


Place the dataset file slim enc mg.csv in the same folder as the script.

Open a terminal or command prompt in the project folder.

Run the script:

python auranet_model.py


Enter user details when prompted (age, symptoms, lifestyle inputs).

Wait for the model to compute MSS, ASS, and OSI scores.

View severity classification (Normal / Medium / Severe).

Check the automatically displayed plots (MSS, ASS, OSI, comparison scatter).

Read the personalized lifestyle suggestions printed at the end.

### **At Runtime:**
You’ll be prompted to enter:
- Demographic data (Age, Frequency, Duration, etc.)
- Binary symptom indicators (Nausea, Vomit, Photophobia, etc.)
- Lifestyle attributes (Sleep, Hydration, Exercise, Sunlight)

The system will:
1. Compute **MSS, ASS, OSI** scores  
2. Match the input to the dataset (using Euclidean distance for nearest similarity)  
3. Predict the severity class  
4. Display **visual plots** comparing actual vs predicted trends  
5. Provide **personalized lifestyle suggestions**

---

## Sample Output
```
🧠 User 1 Predicted Scores → MSS: 2.45, ASS: 1.15, OSI: 2.80
Predicted Severity → Severe
Actual Severity → Medium

=== 🧾 Lifestyle Suggestions for User 1 (Severe) ===
- 🚨 Severe migraine risk: Consult a neurologist immediately.
- 💤 Ensure consistent 7-8 hrs sleep.
- 💧 Stay hydrated (2-3L water daily).
- 🧘 Manage stress: Yoga/meditation recommended.
```

---

## Visualization Outputs
The script automatically generates:
- Actual vs Predicted plots for **MSS**, **ASS**, and **OSI**
- Model comparison scatter plots (Neural Network, Linear Regression, etc.)
- Severity trend distributions  

---

##  Model Performance
| Model | Accuracy | Precision | Recall | F1-score |
|--------|-----------|------------|---------|----------|
| **TabPFN** | 90.00% | 88.15% | 78% | 78.77% |
| **LightGBM** | 88.75% | 86.40% | 76% | 77.10% |
| **CATBoost** | 87.50% | 84.90% | 74% | 75.50% |

> TabPFN demonstrated superior generalization and accuracy for migraine forecasting.

---

## Author
**Saktheshwaran T**  
Vellore Institute of Technology, Vellore  

