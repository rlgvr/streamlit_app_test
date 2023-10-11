import streamlit as st
import pandas as pd
import time
import requests
import io

def oxygen_level_message(oxygen_level):
    if oxygen_level >= 95:
        return "Your oxygen level is within the normal range."
    elif 90 <= oxygen_level < 95:
        return "Your oxygen level is slightly below the normal range. It is advisable to consult a healthcare professional for evaluation."
    elif 85 <= oxygen_level < 90:
        return "Your oxygen level is below the normal range (Hypoxemia). Please seek immediate medical attention."
    else:
        return "Your oxygen level is critically low. Urgent medical attention is required."

st.title("CSV Data Analyzer")

# Use the raw URL of the CSV data in the Git repository
csv_url = "https://github.com/rlgvr/streamlit_app_test/blob/main/simulated_oxygen_level.csv"

# Download the CSV data
response = requests.get(csv_url)

if response.status_code == 200:
    data = pd.read_csv(io.StringIO(response.text), index_col=0)

    st.subheader("Data Preview")
    st.write(data)

    st.subheader("Select a Column to Analyze")

    # Create a radio button to choose a column name
    column_selector = st.radio("Select Column", data.columns)

    if column_selector in data.columns:
        selected_column = data[column_selector]
        max_value = None
        min_value = None
        max_min_table = st.empty()
        table_component = st.empty()
        output_table = st.empty()
        oxygen_message = st.empty()

        if st.button("Start Viewing Rows"):
            for i in range(len(selected_column)):
                table_component.table(data.iloc[i:i+1])  # Display the entire row
                time.sleep(2)

                current_value = selected_column.iloc[i]
                if max_value is None or current_value > max_value:
                    max_value = current_value
                if min_value is None or current_value < min_value:
                    min_value = current_value

                max_min_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))
                oxygen_message.text_area(f"Oxygen Level Message {i}", oxygen_level_message(current_value), height=100)

            st.write("Viewing completed.")
            output_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))
    else:
        st.warning("Selected column does not exist in the DataFrame.")
else:
    st.warning("Failed to retrieve data from the Git repository. Please check the URL.")
