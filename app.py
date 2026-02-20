import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Simple Dashboard", page_icon="📊", layout="wide")

# --- Title ---
st.title("📊 Simple Interactive Dashboard")
st.markdown("A simple Streamlit app with charts, data, and interactivity.")

st.divider()

# --- Sidebar ---
st.sidebar.header("⚙️ Settings")
num_points = st.sidebar.slider("Number of Data Points", 10, 200, 50)
chart_type = st.sidebar.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
show_table = st.sidebar.checkbox("Show Data Table", value=True)
color = st.sidebar.color_picker("Pick a Chart Color", "#4F8BF9")

# --- Generate Random Data ---
np.random.seed(42)
data = pd.DataFrame({
    "Index": range(num_points),
    "Sales": np.random.randint(100, 1000, num_points),
    "Profit": np.random.randint(50, 500, num_points),
    "Expenses": np.random.randint(30, 400, num_points),
})

# --- Metrics Row ---
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${data['Sales'].sum():,}", f"+{data['Sales'].mean():.1f} avg")
col2.metric("📈 Total Profit", f"${data['Profit'].sum():,}", f"+{data['Profit'].mean():.1f} avg")
col3.metric("💸 Total Expenses", f"${data['Expenses'].sum():,}", f"-{data['Expenses'].mean():.1f} avg")

st.divider()

# --- Chart ---
st.subheader(f"{chart_type}")

if chart_type == "Line Chart":
    st.line_chart(data.set_index("Index")[["Sales", "Profit", "Expenses"]])
elif chart_type == "Bar Chart":
    st.bar_chart(data.set_index("Index")[["Sales", "Profit", "Expenses"]])
elif chart_type == "Area Chart":
    st.area_chart(data.set_index("Index")[["Sales", "Profit", "Expenses"]])

st.divider()

# --- Data Table ---
if show_table:
    st.subheader("📋 Data Table")
    st.dataframe(data, use_container_width=True)

# --- User Input Section ---
st.divider()
st.subheader("✍️ Add a Note")
name = st.text_input("Your Name")
note = st.text_area("Your Note")
if st.button("Submit"):
    if name and note:
        st.success(f"✅ Thanks, **{name}**! Your note has been recorded:")
        st.info(f'"{note}"')
    else:
        st.warning("Please fill in both fields.")

# --- Footer ---
st.divider()
st.caption("Built with ❤️ using Streamlit")