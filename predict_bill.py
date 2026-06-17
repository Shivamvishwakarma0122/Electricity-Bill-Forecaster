import joblib

model = joblib.load(
    "../models/bill_model.pkl"
)

units = float(
    input("Enter Units Consumed: ")
)

ac_hours = float(
    input("Enter AC Hours: ")
)

fan_hours = float(
    input("Enter Fan Hours: ")
)

family_members = int(
    input("Enter Family Members: ")
)

prediction = model.predict(
    [[
        units,
        ac_hours,
        fan_hours,
        family_members
    ]]
)

print(
    "\nPredicted Bill Amount = ₹",
    round(prediction[0], 2)
)