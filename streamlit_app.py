import streamlit as st
import pandas as pd
import time

# Function to perform some action based on the selected values
def perform_action(selected_values):
    # Replace this with your custom logic
    if selected_values.mean() < 50:
        return "Low Values"
    else:
        return "High Values"

st.title("CSV Data Analyzer")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, index_col=1)
    #data = data.drop(columns='Unknown:0')

    st.subheader("Data Preview")
    st.write(data)

    st.subheader("Select a Column to Analyze")

    # Create radio buttons to choose a column name
    column_selector = st.radio("Select Column", data.columns)

    if column_selector in data.columns:  # Check if the selected column exists
        # Display the selected column
        selected_column = data[column_selector]

        table_component = st.empty()

        if st.button("Start Viewing Rows"):
            for i in range(len(selected_column)):
                table_component.table(selected_column.iloc[i:i+1])
                time.sleep(2)  # Sleep for 2 seconds between rows

            st.write("Viewing completed.")
    else:
        st.warning("Selected column does not exist in the DataFrame.")

else:
    st.warning("Please upload a CSV file.")
