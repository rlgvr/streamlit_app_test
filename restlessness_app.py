import streamlit as st
import pandas as pd
import time

# Sample DataFrame (replace with your data)
data = {
    'epoch (ms)': [1696967617982, 1696967618062, 1696967618142, 1696967618222, 1696967618302],
    'time (-00:00)': ['2023-10-10T20:53:37.982', '2023-10-10T20:53:38.062', '2023-10-10T20:53:38.142', '2023-10-10T20:53:38.222', '2023-10-10T20:53:38.302'],
    'x-axis (g)': [-0.959, -1.003, -0.971, -0.993, -0.987],
    'y-axis (g)': [-0.252, -0.247, -0.267, -0.264, -0.257],
    'z-axis (g)': [0.134, 0.150, 0.160, 0.165, 0.170],
    'score': [5, 6, 5, 6, 5],
    'Restlessness_Score': [5, 6, 5, 6, 5],
    'Restlessness_Description': [
        'Moderate to High Restlessness',
        'High Restlessness',
        'Moderate to High Restlessness',
        'High Restlessness',
        'Moderate to High Restlessness'
    ]
}

# Convert the 'time (-00:00)' column to timestamp
data['time (-00:00)'] = pd.to_datetime(data['time (-00:00)'])

# Create a Streamlit app
st.title("Streamlit Data Reader")

# Create a button to start reading the data
if st.button("Start"):
    data_index = 0

    # Create a table to show 'x', 'y', and 'z' values
    st.subheader("Current Values")
    values_table = st.table(data[["x-axis (g)", "y-axis (g)", "z-axis (g)"]].iloc[data_index])

    # Create a graph to visualize 'x', 'y', and 'z' values
    st.subheader("Visualization")
    chart = st.line_chart(data[["x-axis (g)", "y-axis (g)", "z-axis (g)"]].iloc[:data_index + 1])

    # Create a text box to show 'Restlessness_Description'
    st.subheader("Restlessness Description")
    description_text = st.text_area("", data["Restlessness_Description"].iloc[data_index])

    while data_index < len(data) - 1:
        data_index += 1

        # Update the table with the next row of data
        values_table.table(data[["x-axis (g)", "y-axis (g)", "z-axis (g)"]].iloc[data_index])

        # Update the visualization with the new row of values
        chart.line_chart(data[["x-axis (g)", "y-axis (g)", "z-axis (g)"]].iloc[:data_index + 1])

        # Update the text box with 'Restlessness_Description' for the current row
        description_text.text(data["Restlessness_Description"].iloc[data_index])

        # Sleep for 1 second before showing the next row
        time.sleep(1)
