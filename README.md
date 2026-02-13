# 💼 Employee Salary Prediction using Machine Learning

## 📌 Project Overview

This project predicts an employee’s salary based on multiple factors such as experience, education level, job role, and number of skills using Machine Learning regression techniques.

The system is trained on a multi-feature dataset and deployed as an interactive web application using Streamlit.

---

## 🎯 Objectives

* Predict salary using regression models
* Perform Exploratory Data Analysis (EDA)
* Encode categorical variables
* Train and evaluate ML model
* Deploy model using Streamlit

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Encoding
5. Model Training (Linear Regression)
6. Model Evaluation
7. Model Saving (.pkl)
8. Web App Deployment

---

## 📊 Dataset Features

| Feature    | Description                |
| ---------- | -------------------------- |
| Experience | Years of work experience   |
| Education  | Bachelors / Masters / PhD  |
| Role       | Junior / Mid / Senior      |
| Skills     | Number of technical skills |
| Salary     | Annual salary (Target)     |

Dataset size: 200 rows

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

## 📈 Model Used

**Multiple Linear Regression**

The model learns the relationship:

Salary = f(Experience + Education + Role + Skills)

---

## 📊 Evaluation Metrics

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🌐 Streamlit Web App Features

* User input sliders & dropdowns
* Real-time salary prediction
* Multi-feature input support
* Interactive UI

---

## ▶️ How to Run the Project

###    Install Requirements

```bash
pip install -r requirements.txt
```

---

###   Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
salary-predictor/
│
├── salary_prediction_model.ipynb
├── data/    
         ├── Salary_dataset.csv
├── salary_model.pkl
├── edu_encoder.pkl
├── role_encoder.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Add more features (location, company size)
* Try advanced models (Random Forest, XGBoost)
* Deploy on Streamlit Cloud
* Add salary visualization dashboard

---

## 🎓 Learning Outcomes

* Regression modeling
* Feature engineering
* Model evaluation
* ML deployment
* End-to-end project building

---

## 👩‍💻 Author

**Nivedita Shill**
Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
