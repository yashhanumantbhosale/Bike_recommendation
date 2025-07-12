import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("bikes.csv")

# App Title
st.title("🏍️ Bike Recommendation App")

# Sidebar Inputs
st.sidebar.header("🔍 Filter Your Preferences")

budget = st.sidebar.slider("Select Budget Range (₹)", 50000, 300000, (70000, 150000))
mileage = st.sidebar.slider("Minimum Mileage (km/l)", 30, 80, 45)
engine = st.sidebar.selectbox("Select Engine Capacity", ["Any"] + sorted(df["Engine"].unique().tolist()))

# Filter Logic
filtered = df[
    (df["Price"] >= budget[0]) &
    (df["Price"] <= budget[1]) &
    (df["Mileage"] >= mileage)
]

if engine != "Any":
    filtered = filtered[filtered["Engine"] == engine]

# Results
st.subheader("📋 Recommended Bikes")

if not filtered.empty:
    for _, row in filtered.iterrows():
        st.markdown(f"### {row['Brand']} {row['Model']}")
        st.write(f"💰 Price: ₹{row['Price']}")
        st.write(f"⚙️ Engine: {row['Engine']}")
        st.write(f"⛽ Mileage: {row['Mileage']} km/l")
        st.write(f"🏷️ Type: {row['Type']}")
        st.markdown("---")
else:
    st.warning("No bikes found matching your preferences.")
