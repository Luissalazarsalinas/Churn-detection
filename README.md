# Churn detection

# **Loan Default Prediction**

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/platform)

An end-to-end Machine Learning Project to detect customer churn.

## **Problem Statement**
The globalization and advancements of telecommunication industry, exponentially raises the number of operators in the market that escalates the competition. In this competitive era, it has become mandatory to maximize the proﬁts periodically, for that various strategies have been proposed, namely, acquiring newcustomers, up-selling the existing customers & increasing the retention period of existing customers. Among all the strategies, retention of existing customers is least expensive as compared to others. In order to adopt the third strategy, companies have to reduce the potential customer churn. In this sense, the main reason of churn is the dissatisfaction of consumer service and support system. The key to unlock solutions to this problem is by forecasting the customers which are at risk of churning.

Therefore, in this project we develop a Streamlit App that utilizes a Machine Learning model(XGBoost) as an API to detect whether the customers from a Telco company will churns or not the company, based on the following criteria: Gender, Partner, Dependents, Tenure Months, Multiple Lines, Internet Service, Online Security, 
Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies, Contract, Payment Method, Monthly Charge, CLTV. 

The App can be viewed through this [link](https://loan-default-app.herokuapp.com/)

## **Data Preparation**
The IBM's Telco customers dataset contains information about a fictional telco company that provid home phone and internet services to 7043 customers in California. It indicates which customers have left, stayed, or signed up for their service. Multiple important demographics are included for each customer, as well as a Satisfaction Score, Churn Score, and Customer Lifetime Value (CLTV) index, whit a total of 32 features or predictor variables include in this dataset.

Preprocessing steps:


Source: [IBM]())


[Dataset link](https://amstat.tandfonline.com/doi/full/10.1080/10691898.2018.1434342)

## **Modelling**

In this project 3 different classification algorithms were tested namely:
- Logistic Regression (Base Line)
- Random Forest
- Extra Tree
- XGBoots

The final model used for the App was the XGBoost Classifier model which had an accuracy score of 0.95 and an ROC-AUC score of 0.94

# **Deploy**
The Streamlit App was deployed on Heroku
