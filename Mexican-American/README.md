# Latin American Spirometry Reference Calculator

This repository contains Python functions and resources used to calculate reference spirometry values for Latin American populations based on weighted data from published studies.

## 📄 Overview
- Reference equations based on studies from Brazil, Mexico, Chile, Uruguay, and Venezuela.
- Predicts FEV1, FVC, FEV1/FVC%, PEFR, FEF25-75, FEF50, FEF75.
- Includes LLN and ULN calculations where applicable.

## 🚀 Getting Started

1. Clone the Repository
bash
git clone https://github.com/yourusername/latin-spirometry.git
cd latin-spirometry

2. Install Dependencies
pip install -r requirements.txt

4. Run a Sample Prediction
from spirometry import predict_fev1, predict_fvc
# Example input
age = 45
height = 170
sex = "male"
fev1_pred = predict_fev1(age, height, sex)
fvc_pred = predict_fvc(age, height, sex)
print("FEV1 Predicted:", fev1_pred)

 Files
spirometry.py — Contains all the reference equations
input.csv - example file for input for Latin American population
README.md — Project documentation

 Requirements
Python 3.7+
numpy
pandas
