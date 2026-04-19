import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Page config
st.set_page_config(
page_title="Lead Conversion Predictor",
page_icon="📊",
layout="wide"
)

# Load files
model = pickle.load(open("rf.pkl","rb"))
scaler = pickle.load(open("x_ss.pkl","rb"))

with open("model_columns.pkl","rb") as f:
    columns = pickle.load(f)

# Title
st.title("📊 Customer Lead Conversion Prediction")
st.write("Predict whether a customer will convert")

# Sidebar inputs
st.sidebar.header("Customer Details")

time_spent = st.sidebar.number_input(
"Total Time Spent on Website",
0)

total_visits = st.sidebar.number_input(
"Total Visits",
0)

page_views = st.sidebar.number_input(
"Page Views Per Visit",
0.0)

lead_origin = st.sidebar.selectbox(
"Lead Origin",
["API","Landing Page Submission","Lead Add Form"]
)

lead_source = st.sidebar.selectbox(
"Lead Source",
["Google","Direct Traffic",
"Olark Chat","Organic Search","Reference"]
)

last_activity = st.sidebar.selectbox(
"Last Activity",
["Email Opened",
"SMS Sent",
"Olark Chat Conversation",
"Page Visited"]
)

occupation = st.sidebar.selectbox(
"Occupation",
["Unemployed",
"Working Professional",
"Student"]
)

tags = st.sidebar.selectbox(
"Tags",
["Interested",
"Will revert",
"Busy",
"Closed"]
)

lead_quality = st.sidebar.selectbox(
"Lead Quality",
["High","Medium","Low","Might be"]
)

last_notable = st.sidebar.selectbox(
"Last Notable Activity",
["Modified",
"Email Opened",
"SMS Sent"]
)

specialization = st.sidebar.selectbox(
"Specialization",
["Management",
"Business Administration",
"IT Projects",
"Finance",
"Marketing"]
)

# Prediction button
if st.sidebar.button("Predict Conversion"):

    input_data = pd.DataFrame(
        np.zeros((1,len(columns))),
        columns=columns)

    input_data['Total Time Spent on Website'] = time_spent
    input_data['TotalVisits'] = total_visits
    input_data['Page Views Per Visit'] = page_views

    def set_col(name):
        if name in input_data.columns:
            input_data[name] = 1

    set_col('Lead Origin_'+lead_origin)
    set_col('Lead Source_'+lead_source)
    set_col('Last Activity_'+last_activity)
    set_col('What is your current occupation_'+occupation)
    set_col('Tags_'+tags)
    set_col('Lead Quality_'+lead_quality)
    set_col('Last Notable Activity_'+last_notable)
    set_col('Specialization_'+specialization)

    input_scaled = scaler.transform(input_data)

    pred = model.predict(input_scaled)

    prob = model.predict_proba(input_scaled)

    st.subheader("Prediction Result")

    col1,col2 = st.columns(2)

    if pred[0]==1:
        col1.success("Customer will Convert ✅")
    else:
        col1.error("Customer will NOT Convert ❌")

    col2.info(
    "Conversion Probability: "
    +str(round(prob[0][1]*100,2))+"%"
    )

# Footer
st.write("---")
st.write("ML Model: Random Forest | Training Accuracy: 99%")