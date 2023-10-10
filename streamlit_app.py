import streamlit as st
import pandas as pd

# Function to perform some action based on the selected value
def perform_action(selected_value):
    # Replace this with your custom logic
    if selected_value < 50:
        return "Low Value"
    else:
        return "High Value"

st.title("CSV Data Analyzer")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(data)

    st.subheader("Select a Row to Analyze")

    # Create a selectbox to choose a column name
    column_selector = st.selectbox("Select Column", data.columns)

    # Display the selected column
    selected_column = data[column_selector]
    st.write("Selected Column:")
    st.write(selected_column)

    # Perform an action based on the selected values
    selected_values = data[column_selector]  # Use the selected column
    output = perform_action(selected_values)
    st.write("Output based on the selected values:")
    st.write(output)

else:
    st.warning("Please upload a CSV file.")
