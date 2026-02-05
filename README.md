# 🌴 Plantation Analytics Dashboard

End-to-end data analytics project simulating plantation business performance.
This project demonstrates a complete analytics pipeline — from raw data generation, ETL processing, SQL analytics, data modeling, and interactive dashboard deployment.

🔗 Live Dashboard:
https://plantationanalyticsproject-3nqeyte7kik6hvfg9bvrdq.streamlit.app/


## 📌 Project Objective

The goal of this project is to simulate a real-world business analytics workflow and answer key management questions:

- Which region generates the highest profit?
- How does profit trend over time?
- Is operational cost efficient?
- Does higher production always increase profit?
- How does inventory impact profitability?

This project mimics how a data analyst supports executive decision-making.


## 🛠 Tools & Technologies

- Python (Pandas, NumPy)
- SQL (SQLite + SQLAlchemy)
- Data Visualization (Matplotlib, Seaborn, Plotly)
- Streamlit (Interactive dashboard)
- GitHub (Version control)
- Jupyter Notebook (EDA & analytics)


## 📂 Project Structure

plantation_analytics_project/
│
├── data/ # Raw and processed datasets
├── notebooks/ # EDA and analysis notebooks
├── src/ # ETL and analytics scripts
├── dashboard/
│ ├── app.py # Streamlit dashboard
│ └── plantation.db # SQLite database
│
├── requirements.txt
└── README.md


## 🔄 Pipeline Overview

1. **Data Generation**
   - Synthetic plantation dataset created to simulate business operations

2. **Data Cleaning (ETL)**
   - Missing values handled
   - Data standardized
   - Metrics engineered (profit margin)

3. **SQL Analytics**
   - Business queries written to analyze performance
   - Region comparison
   - Monthly trends
   - Efficiency analysis

4. **Data Modeling**
   - Structured for analytical queries
   - Fact-style dataset optimized for dashboard

5. **Dashboard Development**
   - KPI cards
   - Interactive filters
   - Trend analysis
   - Correlation heatmap
   - Executive insight summary

6. **Deployment**
   - Streamlit Cloud deployment
   - Public dashboard link

## 📊 Dashboard Features

- Executive KPI summary
- Region profitability analysis
- Monthly profit trends
- Profit distribution visualization
- Correlation heatmap
- Interactive filters
- Automated business insights

The dashboard is designed for management-level decision support.

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
cd dashboard
streamlit run app.py

