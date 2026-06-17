# ⚡ Electricity Bill Forecaster

A Machine Learning-based web application that predicts monthly electricity bills using household electricity consumption data such as Units Consumed, AC Usage Hours, Fan Usage Hours, and Number of Family Members.

The project uses **Linear Regression** for prediction and **Streamlit** for creating an interactive dashboard with visual analytics.

---

## 🚀 Features

* Predict Electricity Bills Instantly
* Interactive Streamlit Dashboard
* Manual User Input
* Electricity Consumption Analysis
* Bill Prediction Using Machine Learning
* Dataset Statistics
* Data Visualization
* User-Friendly Interface
* Real-Time Prediction Results

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Joblib

---

## 📊 Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values. The model learns the relationship between electricity consumption factors and the final electricity bill amount and generates predictions for future usage.

---

## 📁 Dataset Features

| Feature        | Description                  |
| -------------- | ---------------------------- |
| Units Consumed | Total Electricity Units Used |
| AC Hours       | Daily AC Usage Hours         |
| Fan Hours      | Daily Fan Usage Hours        |
| Family Members | Number of Household Members  |

### Target Variable

| Variable    | Description              |
| ----------- | ------------------------ |
| Bill Amount | Monthly Electricity Bill |

---

## 📂 Project Structure

```text
Electricity_Bill_Forecaster/
│
├── data/
│   └── electricity_data.csv
│
├── models/
│   └── bill_model.pkl
│
├── app.py
├── generate_data.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shivamvishwakarma0122/Electricity-Bill-Forecaster.git
```

Move into the project folder:

```bash
cd Electricity-Bill-Forecaster
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run:

```bash
python generate_data.py
python train_model.py
```

This generates:

```text
electricity_data.csv
bill_model.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 📈 Dashboard Components

### Statistics Cards

* Total Records
* Average Electricity Bill
* Average Units Consumed
* Model Information

### Bill Prediction

Users can enter:

* Units Consumed
* AC Usage Hours
* Fan Usage Hours
* Number of Family Members

and receive an estimated electricity bill.

### Visualizations

* Units Consumed vs Bill Amount Scatter Plot
* Electricity Consumption Analysis
* Dataset Statistics

### Dataset Preview

Displays the electricity consumption dataset used for training.

---

## 🎯 Project Objective

The objective of this project is to develop a machine learning model capable of estimating monthly electricity bills based on household electricity consumption patterns. The system helps users understand how energy usage affects electricity costs and assists in planning and managing household expenses efficiently.

---

## 📊 Application Features

✔ Interactive Dashboard

✔ Electricity Bill Prediction

✔ Machine Learning-Based Forecasting

✔ Data Analytics & Insights

✔ Graphical Visualizations

✔ User-Friendly Interface

---

## 🔮 Future Scope

* Real Electricity Tariff Integration
* Weather-Based Consumption Forecasting
* Smart Meter Integration
* Monthly Usage Trend Analysis
* PDF Report Generation
* Advanced Machine Learning Models

---

## 👨‍💻 Author

**Shivam Vishwakarma**

Minor Project: **Electricity Bill Forecaster**

GitHub Profile:

https://github.com/Shivamvishwakarma0122

Project Repository:

https://github.com/Shivamvishwakarma0122/Electricity-Bill-Forecaster

---
