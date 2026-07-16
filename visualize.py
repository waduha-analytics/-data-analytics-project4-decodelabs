import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Cleaned_Dataset.csv')
print(df.shape)
print(df.columns.tolist())
# Product-wise Total Revenue
product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
print(product_revenue)

plt.figure(figsize=(9,5))
product_revenue.plot(kind='bar', color='#2F5233')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart1_bar_revenue.png')
print("✅ Bar chart saved")

# Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', color='#2F5233')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_line_monthly.png')
print("✅ Line chart saved")

# Payment Method Distribution
payment_dist = df['PaymentMethod'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(payment_dist, labels=payment_dist.index, autopct='%1.1f%%',
        colors=['#2F5233', '#5B8C5A', '#8FBC8F', '#B5D8B5'])
plt.title('Orders by Payment Method')
plt.tight_layout()
plt.savefig('chart3_pie_payment.png')
print("✅ Pie chart saved")

# Step 1: Product-wise revenue nikालो aur sort karo (descending)
product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

# Step 2: Cumulative percentage calculate karo
cumulative_pct = product_revenue.cumsum() / product_revenue.sum() * 100

# Step 3: Pareto chart banao
fig, ax1 = plt.subplots(figsize=(10,6))

ax1.bar(product_revenue.index, product_revenue.values, color='#2f5233')
ax1.set_xlabel('Product')
ax1.set_ylabel('Total Revenue')
ax1.tick_params(axis='x', rotation=45)

ax2 = ax1.twinx()
ax2.plot(product_revenue.index, cumulative_pct.values, color='red', marker='o')
ax2.set_ylabel('Cumulative %')
ax2.set_ylim(0, 110)
ax2.axhline(80, color='gray', linestyle='--')  # 80% reference line

plt.title('No Dominant Product: Revenue Spread Almost Evenly Across Catalog')
plt.tight_layout()
plt.savefig('chart4_pareto_revenue.png')
plt.show()