import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    "data/electricity_data.csv"
)

X = df[
    [
        "Units_Consumed",
        "AC_Hours",
        "Fan_Hours",
        "Family_Members"
    ]
]

y = df["Bill_Amount"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(
    model,
    "models/bill_model.pkl"
)

print("Model Saved Successfully")