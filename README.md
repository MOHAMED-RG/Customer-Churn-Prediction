# 📊 Customer Churn Prediction using Machine Learning

## Overview

This project focuses on predicting customer churn using Machine Learning.

The project follows an end-to-end Machine Learning workflow, including data cleaning, exploratory data analysis, preprocessing, model training, model comparison, evaluation, and Streamlit deployment.

---

## Project Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Correlation Analysis
5. Data Preprocessing
6. Model Training
7. Model Comparison
8. Model Evaluation
9. Feature Importance
10. Streamlit Deployment

---

## Objectives

- Understand customer churn patterns.
- Explore relationships between customer features and churn.
- Clean and preprocess the dataset.
- Train different classification models.
- Compare model performance.
- Select the best-performing model based on the observed test results.
- Analyze feature importance.
- Deploy the final model using Streamlit.

---

## Dataset

The dataset was obtained from Kaggle:

[Customer Churn Prediction: Analysis](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis)

### Dataset Information

- **Rows:** 1,000
- **Columns:** 10
- **Target:** Churn

### Main Features

- `Age`
- `Tenure`
- `MonthlyCharges`
- `TotalCharges`
- `Gender`
- `ContractType`
- `InternetService`
- `TechSupport`
- `Churn`

---

## Exploratory Data Analysis

The dataset contains:

- **883 customers** who did not churn.
- **117 customers** who churned.

This shows that the target variable is imbalanced, with fewer customers in the churn class.

EDA was used to understand:

- Customer demographics
- Contract types
- Internet services
- Tech support
- Monthly charges
- Total charges
- Tenure
- Churn distribution

---

## Data Cleaning

The following preprocessing steps were performed:

- Missing values in `InternetService` were replaced with `None`.
- The `Churn` column was encoded:
  - `Yes` → `1`
  - `No` → `0`
- `CustomerID` was removed because it is an identifier and does not provide useful predictive information.

---

## Correlation Analysis

Correlation analysis was used to understand relationships between numerical variables.

Some notable correlations were:

- `Tenure` and `TotalCharges` → approximately **0.89**
- `Tenure` and `Churn` → approximately **-0.22**
- `MonthlyCharges` and `Churn` → approximately **0.17**

These correlations provide an initial understanding of relationships between customer features and churn.

![Correlation Heatmap](correlation_heatmap.png)
---

## Data Preprocessing

The data preprocessing steps included:

- Handling missing values
- Encoding the target variable
- One-hot encoding categorical variables
- Removing `CustomerID`
- Splitting the dataset into training and testing sets
- Scaling features for Logistic Regression

### Example Encoded Features

After one-hot encoding, categorical variables were converted into features such as:

- `Gender_Male`
- `ContractType_One-Year`
- `ContractType_Two-Year`
- `InternetService_Fiber Optic`
- `InternetService_None`
- `TechSupport_Yes`

The dataset was split into:

- **80% Training Data**
- **20% Testing Data**

---

## Machine Learning Models

Three classification models were trained and evaluated:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Decision Tree

Used to capture nonlinear relationships between the features and the target.

### 3. Random Forest

An ensemble learning algorithm used for classification and feature importance analysis.

---

## Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 95.5% | 0.95 | 0.95 | 0.95 | 0.985 |
| Decision Tree | 99.5% | 0.99 | 0.99 | 0.99 | 0.997 |
| Random Forest | 100% | 1.00 | 1.00 | 1.00 | 1.000 |

---

## Model Selection

Based on the observed test-set results, **Random Forest** achieved the highest performance among the tested models.

Therefore, Random Forest was selected as the final model for the Streamlit application.

> **Note:** The perfect test performance is unusually high. Further validation should be performed to check for possible data leakage, dataset construction issues, or overfitting.

---

## Model Evaluation

The Random Forest model achieved:

- **Accuracy:** 100%
- **Precision:** 1.00
- **Recall:** 1.00
- **F1-Score:** 1.00
- **ROC-AUC:** 1.000

### Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

The test set contained 200 samples.

|  | Predicted No Churn | Predicted Churn |
|---|---:|---:|
| Actual No Churn | 177 | 0 |
| Actual Churn | 0 | 23 |

This resulted in:

- **True Negatives (TN):** 177
- **True Positives (TP):** 23
- **False Positives (FP):** 0
- **False Negatives (FN):** 0

---

## ROC-AUC

The Random Forest model achieved an ROC-AUC score of **1.000** on the test set.

![ROC Curve](roc_curve.png)

ROC-AUC measures the model's ability to distinguish between customers who churn and customers who do not churn.

---

## Feature Importance

The Random Forest model was also used to identify the most important features.

![Feature Importance](feature_importance.png)

The main features included:

1. `Tenure`
2. `ContractType_One-Year`
3. `TechSupport_Yes`
4. `MonthlyCharges`
5. `ContractType_Two-Year`
6. `TotalCharges`

Feature importance shows which features contributed most to the model's predictions.

> **Note:** Feature importance is model-specific and should not be interpreted as proof of a causal relationship.
---

## Streamlit Deployment

The trained Random Forest model was integrated into a Streamlit application.

### Application Workflow

```text
Customer Input
      ↓
Data Preprocessing
      ↓
Random Forest Model
      ↓
Churn Prediction
      ↓
Prediction Probability

```
### Streamlit Features

- Customer input form
- Churn prediction
- Prediction probability
- Random Forest model
- Simple and interactive interface

### Application Preview

![Streamlit Application](streamlit_app.png)

### Live Demo

[🚀 Try the Customer Churn Prediction App](https://customer-churn-prediction-yc2ddshjwu5cayzmmsqk34.streamlit.app/)

### Run Locally

Install the required libraries:

```bash
pip install -r requirements.txt

```

## Tools Used

### Programming & Data Analysis
- Python
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Joblib

### Development & Deployment
- Jupyter Notebook
- Streamlit

---

## Project Structure

```text
Customer-Churn-Prediction/
│
├── customer-churn-prediction.ipynb
├── customer_churn_data.csv
├── customer_churn_model.pkl
├── app.py
├── requirements.txt
├── README.md
├── correlation_heatmap.png
├── confusion_matrix.png
├── roc_curve.png
├── feature_importance.png
└── streamlit_app.png
```

### Run Locally

Install the required libraries:

```bash
pip install -r requirements.txt

```

## Future Improvements

- Perform cross-validation.
- Investigate the unusually high test performance.
- Check for possible data leakage.
- Apply hyperparameter tuning using `GridSearchCV`.
- Test additional Machine Learning models.
- Improve the Streamlit interface.
- Add SHAP-based model explanations.

---

## Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting customer churn.

The dataset was cleaned and explored, followed by feature preprocessing and training of three classification models: Logistic Regression, Decision Tree, and Random Forest.

Among the tested models, Random Forest achieved the highest observed test-set performance and was selected for the final application. The model was then integrated into a Streamlit application that allows users to enter customer information and receive a churn prediction with its probability.

The project provided practical experience with data preprocessing, classification models, model evaluation, feature importance, and Machine Learning deployment.

Further validation, including cross-validation and investigation of the unusually high test performance, would be useful before considering the model ready for real-world use.

---

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/api/sklearn.metrics.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
