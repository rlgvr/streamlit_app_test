import streamlit as st
import pandas as pd
import time
import requests

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

# Use the raw URL of the CSV file in the Git repository
csv_url = "https://github.com/rlgvr/streamlit_app_test/blob/main/simulated_oxygen_level.csv"

# Download the CSV file
response = requests.get(csv_url)

if response.status_code == 200:
    data = pd.read_csv(pd.compat.StringIO(response.text), index_col=0)

    st.subheader("Data Preview")
    st.write(data, index=False)

    st.subheader("Select a Column to Analyze")

    # Create radio buttons to choose a column name
    column_selector = st.radio("Select Column", data.columns)

    if column_selector in data.columns:  # Check if the selected column exists
        # Display the selected column
        selected_column = data[column_selector]

        max_value = None
        min_value = None
        max_min_table = st.empty()
        table_component = st.empty()
        output_table = st.empty()  # New table for additional information
        oxygen_message = st.empty()  # Textbox for oxygen level message

        if st.button("Start Viewing Rows"):
            for i in range(len(selected_column)):
                table_component.table(selected_column.iloc[i:i+1])
                time.sleep(2)  # Sleep for 2 seconds between rows

                # Update max and min values
                current_value = selected_column.iloc[i]
                if max_value is None or current_value > max_value:
                    max_value = current_value
                if min_value is None or current_value < min_value:
                    min_value = current_value

                # Display the max and min values in a separate table
                max_min_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))

                # Display oxygen level message with a unique key
                oxygen_message.text_area(f"Oxygen Level Message {i}", oxygen_level_message(current_value), height=100)

            st.write("Viewing completed.")

            # Additional information after viewing
            output_table.table(pd.DataFrame({'Max Value': [max_value], 'Min Value': [min_value]}))
    else:
        st.warning("Selected column does not exist in the DataFrame.")

else:
    st.warning("Failed to retrieve the CSV file from the Git repository. Please check the URL.")
