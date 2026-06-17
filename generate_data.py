import pandas as pd
import random

data = []

for _ in range(1000):

    units = random.randint(100, 700)
    ac_hours = random.randint(0, 12)
    fan_hours = random.randint(5, 18)
    family_members = random.randint(2, 8)

    bill = (
        units * 8
        + ac_hours * 90
        + fan_hours * 20
        + family_members * 50
        + random.randint(-200, 200)
    )

    data.append([
        units,
        ac_hours,
        fan_hours,
        family_members,
        bill
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Units_Consumed",
        "AC_Hours",
        "Fan_Hours",
        "Family_Members",
        "Bill_Amount"
    ]
)

df.to_csv(
    "data/electricity_data.csv",
    index=False
)

print("Dataset Generated Successfully")