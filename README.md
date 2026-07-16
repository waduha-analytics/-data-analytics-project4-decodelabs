# Data Visualization — Project 4
**DecodeLabs Internship | Data Analytics Track | Week 4**

## 📌 Project Overview
This project focuses on visualizing key patterns from a cleaned e-commerce orders dataset (1,200 records) using Python. Four charts were built to explore revenue distribution, sales trends, payment behavior, and revenue concentration — translating raw data into clear, presentation-ready business insights.

## 🎯 Objectives
- Visualize product-wise revenue performance using a bar chart
- Track monthly sales trends over time using a line chart
- Analyze payment method distribution using a pie chart
- Build an executive-level Pareto chart to assess revenue concentration
- Compile all visuals and insights into a professional PDF report

## 🛠️ Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- ReportLab (PDF report generation)

## 📊 Key Findings
| Finding | Detail |
|---|---|
| Top revenue products | Chair and Printer generate the highest total revenue |
| Balanced product performance | Revenue is fairly close across all 7 products — no single item dominates |
| Volatile monthly trend | Sales fluctuate significantly, with a sharp peak around mid-2024 |
| Even payment distribution | Orders are almost evenly split across 5 payment methods (~19–22% each) |
| Weak Pareto pattern | 6 of 7 products needed for 80% of total revenue — no 80/20 concentration |

## 💡 Business Recommendations
- Avoid over-investing in a single "hero product" — revenue is broadly distributed
- Investigate the mid-2024 sales spike to identify and replicate the driving factor
- Continue supporting multiple payment methods — no single method dominates
- Use Pareto view for inventory and marketing prioritization

## 📂 Files in this Repository
- `Cleaned_Dataset.csv` — input dataset (from Project 1)
- `visualize.py` — Python script for generating all charts
- `chart1_bar_revenue.png` — Total Revenue by Product
- `chart2_line_monthly.png` — Monthly Sales Trend
- `chart3_pie_payment.png` — Orders by Payment Method
- `chart4_pareto_revenue.png` — Executive Pareto Analysis
- `Project4_Data_Visualization_Report.pdf` — consolidated PDF report

## 🚀 How to Run
```bash
pip install pandas matplotlib seaborn
python visualize.py
```

## 👤 Author
Waduha — Data Analytics Intern, DecodeLabs
