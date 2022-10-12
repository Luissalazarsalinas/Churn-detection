# **Churn detection**
[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)

An end-to-end Machine Learning Project to detect customer churn.

## **Problem Statement**
The globalization and advancements of telecommunication industry, exponentially raises the number of operators in the market that escalates the competition. In this competitive era, it has become mandatory to maximize the proﬁts periodically, for that various strategies have been proposed, namely, acquiring newcustomers, up-selling the existing customers & increasing the retention period of existing customers. Among all the strategies, retention of existing customers is least expensive as compared to others. In order to adopt the third strategy, companies have to reduce the potential customer churn. In this sense, the main reason of churn is the dissatisfaction of consumer service and support system. The key to unlock solutions to this problem is by forecasting the customers which are at risk of churning.

Therefore, in this project we develop a Streamlit App that utilizes a Machine Learning model(XGBoost) as an API to detect whether the customers from a Telco company will churns or not the company, based on the following criteria: Gender, Partner, Dependents, Tenure Months, Multiple Lines, Internet Service, Online Security, 
Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies, Contract, Payment Method, Monthly Charge, CLTV. 

The App can be viewed through this [link](https://luissalazarsalinas-churn-detection-streamlit-app-r6b54r.streamlitapp.com/)

Machine Learning: [NoteBook](https://github.com/Luissalazarsalinas/Churn-detection/blob/master/NoteBooks/Customer_Churn.ipynb)


## Machine Learning

### **Data Preparation**
The IBM's Telco customers dataset contains information about a fictional telco company that provid home phone and internet services to 7043 customers in California. It indicates which customers have left, stayed, or signed up for their service. Multiple important demographics are included for each customer, as well as a Satisfaction Score, Churn Score, and Customer Lifetime Value (CLTV) index, whit a total of 32 features or predictor variables include in this dataset.

Data preprocessing steps:

- Clean the data: removed duplicate values, missing values, unnecessary and leakage variables
- Transform no-numerical variables to numerical variables
- Split the data into train, validation and test sets
- Handled unbalanced data with oversampling technique - SMOTE
- Select the best set of features using Recursive Feature Elimination with Cross Validation(RFECV) technique 

Source: [IBM](https://community.ibm.com/accelerators/catalog/content/Telco-customer-churn)

### **Modelling**
Machine Learning Algorithms that were tested:
- Logistic Regression (Base Line)
- KNeighbor
- XGBoots

Xgboost was the model with better performance with the validation set:
- Accuracy: 0.93
- F1-Score: 0.90
- ROC-AUC: 0.93

Performance of the final model(XGBoost) with the test set:
- Accuracy: 0.99
- F1-Score: 0.98
- ROC-AUC: 0.98

### **Deployment**
- The Machine learning API was deployed using the Dockerfile on Heroku
- The streamlit app was deployed on Streamlit Cloud and accesses the ML api deployed on Heroku
