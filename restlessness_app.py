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
st.write("Start Live Evaluation")

# Create a table to show the x, y, z values (initially empty)
values_table = st.empty()

# Create a text element for the description and score (initially empty)
description_and_score = st.empty()

# Create a button to start processing
if st.button("Start"):
    # Create an empty line chart for visualization
    chart = st.line_chart(data=pd.DataFrame(columns=["Timestamp_Accel", "X-axis (g)", "Y-axis (g)", "Z-axis (g)"]))

    data_to_plot = pd.DataFrame(columns=["Timestamp_Accel", "X-axis (g)", "Y-axis (g)", "Z-axis (g)"])
    while data_index < len(data):
        # Get current row data
        current_row = data.iloc[data_index]
        x_value = current_row["x-axis (g)"]
        y_value = current_row["y-axis (g)"]
        z_value = current_row["z-axis (g)"]
        description = current_row["Restlessness_Description"]
        score = current_row["score_accelerometer"]
        timestamp = current_row["Timestamp_Accel"]

        # Update time to human-readable format
        current_time = current_row["Timestamp_Accel"]

        # Update the table to show the x, y, z values
        values_table.table(pd.DataFrame({
            "X-axis (g)": [x_value],
            "Y-axis (g)": [y_value],
            "Z-axis (g)": [z_value]
        }))

        # Create a description and score text
        description_text = f"Description: {description}\nScore: {score}"

        # Update description and score text
        description_and_score.text(description_text)

        # Add data to the DataFrame to plot
        data_to_plot = data_to_plot.append({
            "Timestamp_Accel": timestamp,
            "X-axis (g)": x_value,
            "Y-axis (g)": y_value,
            "Z-axis (g)": z_value
        }, ignore_index=True)

        if data_index >= 5:
            chart.line_chart(data=data_to_plot, use_container_width=True, x="Timestamp_Accel")

        # Update index and wait for 1 second before the next row
        data_index += 1
        time.sleep(1)
