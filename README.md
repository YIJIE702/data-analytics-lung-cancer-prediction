# 🫁 **Lung Cancer Prediction – Data Analytics Project**

## 📌 **Project Overview** 
This project aims to analyze and predict the likelihood of lung cancer based on multiple health, lifestyle, and environmental factors. Using **data preprocessing**, **statistical profiling**, and **visualization techniques**, we explore the relationships between key features such as air pollution, smoking habits, chronic lung disease, and cancer severity levels.  
The project provides **insights into high-risk factors**, which can help in early intervention and awareness.  

---

## 🎯 **Objectives**
1. Identify correlations and patterns between features and lung cancer diagnosis.  
2. Create clear and meaningful visualizations to communicate findings to stakeholders.  
3. Determine which features are most important in predicting lung cancer.  

---

## 📊 **Dataset**
- **Name:** Lung Cancer Prediction (cancer_patient_datasets) 
- **Size:** 1,000 records  
- **Features:**  
  - Demographics: Age, Gender  
  - Lifestyle: Alcohol use, Smoking, Passive smoking  
  - Environmental: Air pollution, Occupational hazard, Dust allergy  
  - Medical history & symptoms: Chronic lung disease, Obesity, Chest pain, Fatigue, Weight loss, Snoring, Dry cough, Coughing of blood, Shortness of breath  

The **severity level of lung cancer** is categorized into:
- **Level 1:** Low  
- **Level 2:** Medium  
- **Level 3:** High  

---

## 🛠️ **Methodology** 
### 1️⃣ **Data Preprocessing**
- Checked all values to ensure they are within valid ranges (1–9).  
- Handled missing values (none found in dataset).  
- Converted categorical variables (Low, Medium, High) into numeric values (1, 2, 3).  
- Performed **data profiling** to compute mean, standard deviation, min/max values.  
- Saved processed dataset into `updated_dataset.xlsx`.  

### 2️⃣ **Data Visualization**
Visualizations were created to explore:  
- **Gender Distribution:** Males represent 59.8% of cases, indicating higher risk.  
- **Age Groups:** Ages 26–48 had the highest number of cases.  
- **Air Pollution Levels:** Higher air pollution strongly correlates with cancer severity.  
- **Lifestyle Factors:** Smoking, passive smoking, and alcohol use contribute significantly to risk.  
- **Medical Symptoms:** Chest pain, dry cough, and chronic lung disease show strong association with high severity cancer cases.  
Visualizations were built using **Google Looker Studio**, allowing interactive filtering by severity level.  

### 3️⃣ **Feature Analysis**
- Identified top 10 parameters most correlated with lung cancer:  
  **Chronic lung disease, Air pollution, Dust allergies, Occupational hazards, Alcohol use, Dry cough, Chest pain, Snoring, Smoking, Passive smoker**  
- Found strong links between **Level 7 occupational hazards**, **high dust allergy exposure**, and **high lung cancer severity**.  

---

## 📈**Key Findings**
- **Males** have a significantly higher risk of lung cancer (59.8%) compared to females (40.2%).  
- **Air pollution** and **occupational hazards** are leading external contributors.  
- **Chest pain (Level 7)** is the strongest indicator of high severity lung cancer cases.  
- **Smoking & Passive Smoking (Level 7)** show highest record counts for cancer incidence.  
- **Ages 33–38** are the most affected demographic group.  

---

## 📊 **Google Looker Studio Dashboard**
An interactive dashboard was created to summarize the findings.  
It includes:  
- **Gender and Age Distribution Charts** to visualize affected groups.  
- **Severity Level Filters** allowing users to view Low, Medium, or High cancer severity insights.  
- **Bar Charts and Pie Charts** showing patterns in air pollution, smoking, alcohol use, and medical symptoms.  
- **Feature Comparison Visuals** for identifying which parameters are most strongly associated with lung cancer cases.  
This dashboard consolidates all analysis results into a single, easy-to-understand view, helping stakeholders quickly interpret the data.   

---

📌 **Conclusion**
- This project successfully identified critical risk factors for lung cancer.
- Findings confirm a strong relationship between environmental exposure (air pollution) and lung cancer severity.
- The analysis highlights key symptoms and lifestyle factors that could be used to develop a predictive machine learning model in future research.
---

## 📜 **License**
This project is licensed under the [MIT License](./LICENSE).
