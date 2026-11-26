import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing sales
df = df.dropna(subset=["Sales"])

# Select product A
product_a = df[df["Product"] == "A"]

# Plot graph
plt.plot(product_a["Day"], product_a["Sales"], marker="o")

plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales for Product A")

plt.show()