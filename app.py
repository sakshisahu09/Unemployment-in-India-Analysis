import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Unemployment in India.csv")

# Clean column names if necessary
df.columns = df.columns.str.strip()

st.title("Unemployment in India Analysis")

# User input filters
state = st.selectbox("Select State", df['Region'].dropna().unique())
date = st.selectbox("Select Date", df['Date'].dropna().unique())

# Filtered data
filtered_data = df[(df['Region'] == state) & (df['Date'] == date)]

# Display output
if not filtered_data.empty:
    rate = filtered_data.iloc[0]['Estimated Unemployment Rate (%)']
    st.success(f"📊 Unemployment Rate in {state} on {date}: {rate:.2f}%")
else:
    st.warning("No data available for the selected state and date.")

# Optional: Plot unemployment rate trend for selected state
st.subheader(f"📈 Unemployment Rate Trend for {state}")
state_data = df[df['Region'] == state]
fig, ax = plt.subplots()
ax.plot(state_data['Date'], state_data['Estimated Unemployment Rate (%)'], marker='o')
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
st.pyplot(fig)