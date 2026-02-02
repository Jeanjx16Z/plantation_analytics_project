import pandas as pd
from sqlalchemy import create_engine

# load cleaned data
df = pd.read_csv("C:/Users/JEAN JEASEN/Documents/DataAnalytics/plantation_analytics_project/data/processed/cleaned_data.csv")

# buat SQLite database
engine = create_engine("sqlite:///plantation.db")

# simpan ke database
df.to_sql("plantation", engine, if_exists="replace", index=False)

print("✅ Data loaded to database!")
