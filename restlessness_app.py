!pip install matplotlib
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Load your dataframe
data = pd.read_csv("restlessness_description.csv")

# Initialize index to track the current row
data_index = 0

# Function to convert timestamp to a human-readable format
def convert_timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

# Create a Streamlit app
st.title("Restlessness Data Visualization")
st.write("Click the 'Start' button to visualize data row by row.")

# Create a button to start processing
if st.button("Start"):
    while data_index < len(data):
        # Clear previous content
        st.clear()
        
        # Get current row data
        current_row = data.iloc[data_index]
        x_value = current_row["x-axis (g)"]
        y_value = current_row["y-axis (g)"]
        z_value = current_row["z-axis (g)"]
        description = current_row["Restlessness_Description"]
        
        # Update time to human-readable format
        current_time = convert_timestamp_to_datetime(current_row["epoch (ms)"])
        
        # Create a table to show the x, y, z values
        st.subheader("Current Values")
        values_table = st.table(pd.DataFrame({
            "X-axis (g)": [x_value],
            "Y-axis (g)": [y_value],
            "Z-axis (g)": [z_value]
        }))

        # Create a line chart to visualize the data
        st.subheader("Data Visualization")
        fig, ax = plt.subplots()
        ax.plot(range(data_index, data_index + 1), [x_value], label='X-axis (g)')
        ax.plot(range(data_index, data_index + 1), [y_value], label='Y-axis (g)')
        ax.plot(range(data_index, data_index + 1), [z_value], label='Z-axis (g)')
        ax.set_xlabel("Row")
        ax.set_ylabel("Acceleration (g)")
        ax.set_title(f"Data Visualization at Time: {current_time}")
        ax.legend()
        st.pyplot(fig)
        
        # Show description
        st.subheader("Restlessness Description")
        st.write(description)
        
        # Update index and wait for 1 second before the next row
        data_index += 1
        time.sleep(1)
