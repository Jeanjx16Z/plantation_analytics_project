import pandas as pd
import numpy as np

np.random.seed(42)

rows = 365  # 1 tahun data harian

dates = pd.date_range("2024-01-01", periods=rows, freq="D")

data = {
    "date": dates,
    "region": np.random.choice(["Sumatra", "Kalimantan", "Sulawesi"], rows),
    "production_ton": np.random.randint(80, 200, rows),
    "operational_cost": np.random.randint(2000, 8000, rows),
    "sales_revenue": np.random.randint(7000, 20000, rows),
    "inventory_stock": np.random.randint(100, 600, rows),
}

df = pd.DataFrame(data)

# hitung profit
df["profit"] = df["sales_revenue"] - df["operational_cost"]

# simpan ke raw data
df.to_csv("C:/Users/JEAN JEASEN/Documents/DataAnalytics/plantation_analytics_project/data/raw/plantation_data.csv", index=False)

print("✅ Dataset generated successfully!")
