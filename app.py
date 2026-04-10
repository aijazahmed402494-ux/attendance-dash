import streamlit as st
import pandas as pd
import os

file = "attendance.csv"

if os.path.exists(file):
    df = pd.read_csv(file)
else:
    df = pd.DataFrame(columns=["Name","Code","Department","Status"])

st.title("📊 Attendance Dashboard")

name = st.text_input("Name")
code = st.text_input("Employee Code")
dept = st.text_input("Department")
status = st.selectbox("Status", ["Present", "Leave"])

if st.button("Save"):
    new_data = {
        "Name": name,
        "Code": code,
        "Department": dept,
        "Status": status
    }
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(file, index=False)
    st.success("Saved ✅")

st.dataframe(df)
