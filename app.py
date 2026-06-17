import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Electricity Bill Forecaster",
    page_icon="⚡",
    layout="wide"
)

# Load Model
model = joblib.load("models/bill_model.pkl")

# Load Dataset
df = pd.read_csv("data/electricity_data.csv")

# Title
st.title("⚡ Electricity Bill Forecaster")
st.markdown("---")

st.write(
    "Predict your monthly electricity bill using Machine Learning."
)

# Input Section
st.subheader("🏠 Enter Household Details")

col1, col2 = st.columns(2)

with col1:

    units = st.number_input(
        "Units Consumed",
        min_value=0,
        value=300,
        step=1
    )

    ac_hours = st.number_input(
        "AC Usage Hours Per Day",
        min_value=0,
        max_value=24,
        value=5,
        step=1
    )

with col2:

    fan_hours = st.number_input(
        "Fan Usage Hours Per Day",
        min_value=0,
        max_value=24,
        value=10,
        step=1
    )

    family_members = st.number_input(
        "Number of Family Members",
        min_value=1,
        value=4,
        step=1
    )

st.markdown("")

# Prediction Button
if st.button("🔮 Predict Bill Amount"):

    prediction = model.predict(
        [[
            units,
            ac_hours,
            fan_hours,
            family_members
        ]]
    )

    st.success(
        f"Predicted Electricity Bill: ₹ {prediction[0]:,.2f}"
    )

st.markdown("---")

# Dataset Preview
st.subheader("📊 Dataset Preview")

st.dataframe(df.head(10))

# Visualization
st.markdown("---")

st.subheader("📈 Units Consumed vs Bill Amount")

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    df["Units_Consumed"],
    df["Bill_Amount"]
)

ax.set_xlabel("Units Consumed")
ax.set_ylabel("Bill Amount")
ax.set_title("Electricity Consumption Analysis")

st.pyplot(fig)

# Statistics Section
st.markdown("---")

st.subheader("📋 Dataset Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:
    st.metric(
        "Average Bill",
        f"₹ {df['Bill_Amount'].mean():.2f}"
    )

with col3:
    st.metric(
        "Average Units",
        f"{df['Units_Consumed'].mean():.0f}"
    )

# Footer
st.markdown("---")
st.caption(
    "Developed using Python, Streamlit, Pandas and Scikit-Learn"
)