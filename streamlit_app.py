import json
import requests
import streamlit as st

# Title
st.title("Telco Custumer Churn Detection")

# Image
st.image("img/churn-image.jpeg")
# About
st.write(
    """
    ## ABOUT


    """
)

######################## Funtions ######################
# Binary variables
def create_binary(content):
    if content == "Male":
        content = 1
    elif content == "Female":
        content = 0
    elif content == "Yes":
        content = 1
    elif content == "Not":
        content = 0
    return content
# Covert Multiple Lines, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV and Streaming Movies
def convert_muliples_var(content):
    if content == "No phone service":
        content = 1
    elif content == "Not":
        content = 0
    elif content == "Yes":
        content = 2
    return content

def convert_contract(content):
    if content == "One year":
        content = 1
    elif content == "Month-to-month":
        content = 0
    elif content == "Two year":
        content = 2
    return content

def convert_payment_method(content):
    if content == "Credit card (automatic)":
        content = 1
    elif content == "Bank transfer (automatic)":
        content = 0
    elif content == "Electronic check":
        content = 2
    elif content == "Mailed check":
        content = 3
    return content


########################################################### Inputs ######################################################################
st.sidebar.title("Data Required")

# Categorical and binary variables
var_gender = ("Male", "Female")
var_bool = ("Yes", "Not")
var_multiple = ("No phone service", "Not", "Yes")
var_contract = ("Month-to-month", "One year", "Two year")
var_payment_m = ("Credit card (automatic)", "Bank transfer (automatic)", "Electronic check", "Mailed check")

gender = st.sidebar.selectbox("Gender", var_gender)
partner = st.sidebar.selectbox("Partner", var_bool)
dependents = st.sidebar.selectbox("Dependet", var_bool)
mutiple_lines = st.sidebar.selectbox("Multiple Lines", var_multiple)
internet_services = st.sidebar.selectbox("Internet Services", var_multiple)
online_security = st.sidebar.selectbox("Online Security", var_multiple)
online_backup = st.sidebar.selectbox("Online Backup", var_multiple)
device_protection = st.sidebar.selectbox("Device Protection", var_multiple)
tech_support = st.sidebar.selectbox("Tech Support", var_multiple)
streaming_tv = st.sidebar.selectbox("Streaming TV", var_multiple)
streaming_movies = st.sidebar.selectbox("Streaming Movies", var_multiple)
contract = st.sidebar.selectbox("Contract", var_contract)
paperless_billing = st.sidebar.selectbox("Paperless billing", var_bool)
payment_method = st.sidebar.selectbox("Payment method", var_payment_m)

# Numerical variables
tenure_months = st.sidebar.number_input("Tenure Months", min_value = 0, max_value = 80)
monthly_charges = st.sidebar.number_input("Monthly Charges")
cltv = st.sidebar.number_input("CLTV")

######################################################### Inference #########################################################

prediction = st.button("Detect Result")

if prediction:

    data = {
        "Gender" : create_binary(gender),
        "Parther" : create_binary(partner),
        "Dependents" : create_binary(dependents),
        "Tenure_Months" : tenure_months,
        "Mutiple_lines" : convert_muliples_var(mutiple_lines),
        "Internet_services" : convert_muliples_var(internet_services),
        "Oline_Security" : convert_muliples_var(online_security),
        "Online_Backup" : convert_muliples_var(online_backup),
        "Device_Protection" : convert_muliples_var(device_protection),
        "Tech_support": convert_muliples_var(tech_support),
        "Streaming_tv": convert_muliples_var(streaming_tv),
        "Streaming_movies" : convert_muliples_var(streaming_movies),
        "Contract" : convert_contract(contract),
        "Paperless_billing" : create_binary(paperless_billing),
        "Payment_method": convert_payment_method(payment_method),
        "Monthly_charges" : monthly_charges,
        "cltv": cltv
    }

    # Query
    rep = requests.post("https://churn-detection-app-08.herokuapp.com/predict", json= data)
    json_str = json.dumps(rep.json())
    respon = json.loads(json_str)

    st.subheader(f"{respon[0]}")



