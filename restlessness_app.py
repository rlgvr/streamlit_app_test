import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Load your dataframe
data = pd.read_csv("acc_gyro.csv")

# Initialize index to track the current row
data_index = 0

# Function to convert timestamp to a human-readable format
def convert_timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

# Create a Streamlit app
st.title("Restlessness Evaluation")
start_button = st.button("Start")

if start_button:
    # While the button is not clicked, the code within this block won't execute
    while data_index < len(data):
        # Get current row data
        current_row = data.iloc[data_index]
        x_value = current_row["x-axis (g)"]
        y_value = current_row["y-axis (g)"]
        z_value = current_row["z-axis (g)"]
        description = current_row["Restlessness_Description"]
        score = current_row["score_accelerometer"]
        
        # Update time to human-readable format
        current_time = current_row["Timestamp_Accel"]
        
        # Display the x, y, z values
        st.subheader("Current Values")
        st.table(pd.DataFrame({
            "X-axis (g)": [x_value],
            "Y-axis (g)": [y_value],
            "Z-axis (g)": [z_value]
        }))
        
        # Create a description and score text
        description_text = f"Description: {description}\nScore: {score}"
        
        # Display the description and score text
        st.subheader("Restlessness Description")
        st.text(description_text)
        
        # Display the line chart
        st.subheader("Data Visualization")
        chart_data = pd.DataFrame({
            "Timestamp_Accel": [current_time],
            "X-axis (g)": [x_value],
            "Y-axis (g)": [y_value],
            "Z-axis (g)": [z_value]
        })
        st.line_chart(chart_data)
        
        # Update index and wait for 1 second before the next row
        data_index += 1
        time.sleep(1)
