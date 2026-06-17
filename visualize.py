import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/electricity_data.csv")

plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Units_Consumed',
    y='Bill_Amount',
    data=data
)

plt.title("Units Consumed vs Bill Amount")
plt.xlabel("Units Consumed")
plt.ylabel("Bill Amount")

plt.show()