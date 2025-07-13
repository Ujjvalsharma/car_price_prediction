# 🚗 Car Price Prediction App

This project is a **Machine Learning web application** that predicts the selling price of a car based on various technical specifications using a Linear Regression model. The frontend is built using **Streamlit** and the model is trained using **scikit-learn**.

---

## 📁 Project Structure
car-price-prediction/
│
├── CarPrice.csv # Original dataset from Kaggle
├── car_price_model.pkl # Trained model saved with joblib
├── app.py # Streamlit app for interactive prediction
├── car_price_pre.ipynb 
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🚀 Features

- Clean, interactive UI using Streamlit
- Predict car price based on:
  - Engine size, weight, dimensions
  - Fuel type, aspiration, body style
  - MPG, RPM, compression ratio, etc.
- Supports categorical fields with one-hot encoding
- Trained on dataset from **Kaggle (CarDekho)**

---

## 🧠 Machine Learning Details

- **Model Used**: Linear Regression
- **Libraries**: pandas, numpy, scikit-learn, streamlit
- **Preprocessing**: One-hot encoding of categorical features using `pd.get_dummies()`
- **Evaluation**:
  - R² Score: ~0.89
  - RMSE: ~2912

---

## ▶️ How to Run

1. Clone the repository or download the project
2. Install the required libraries:

```bash
pip install -r requirements.txt
