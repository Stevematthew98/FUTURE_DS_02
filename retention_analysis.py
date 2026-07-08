import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🚀 Initializing Customer Churn Analytics Engine...")

# 1. Load Data
try:
    df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print("-> Success: Raw customer data loaded successfully.")
except FileNotFoundError:
    print("❌ Error: Telco dataset file not found. Please ensure 'WA_Fn-UseC_-Telco-Customer-Churn.csv' is in this directory.")
    exit()

# 2. Data Cleaning & Structural Alignment
print("⚙️ Executing structural data governance checks...")
df['TotalCharges'] = df['TotalCharges'].replace(" ", np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
df = df.dropna(subset=['TotalCharges'])
df['Churn_Numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# 3. High-Impact KPI Matrix Calculations
print("📊 Processing executive-level business metrics...")
total_customers = len(df)
churned_customers = df['Churn_Numeric'].sum()
global_churn_rate = (churned_customers / total_customers) * 100
global_retention_rate = 100 - global_churn_rate
avg_tenure = df['tenure'].mean()
at_risk_revenue = df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()

contract_churn = df.groupby('Contract')['Churn_Numeric'].mean().reset_index()
contract_churn['Churn_Rate_%'] = contract_churn['Churn_Numeric'] * 100

# 4. Generate Visual Reporting Charts
print("🎨 Exporting high-definition analytical visuals...")
sns.set_theme(style="whitegrid")

# Chart A: Contract Type Risk Profile
plt.figure(figsize=(10, 5))
sns.barplot(data=contract_churn, x='Contract', y='Churn_Rate_%', palette='Reds_r')
plt.title('Churn Risk Concentration by Customer Contract Architecture', fontsize=13, pad=15, fontweight='bold')
plt.ylabel('Calculated Churn Rate (%)')
plt.xlabel('Contract Structure')
plt.tight_layout()
plt.savefig('contract_churn_analysis.png', dpi=300)
plt.close()

# Chart B: Tenure Distribution
plt.figure(figsize=(11, 5))
sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', palette=['#1A73E8', '#D93025'], bins=30, kde=True)
plt.title('Customer Lifetime Tenure Density and Churn Attrition Breaks', fontsize=13, pad=15, fontweight='bold')
plt.xlabel('Customer Lifetime Loyalty (Tenure in Months)')
plt.ylabel('Total Account Count')
plt.tight_layout()
plt.savefig('customer_lifetime_distribution.png', dpi=300)
plt.close()

print("🏁 [SYSTEM EXECUTION COMPLETE]: Operational visuals exported flawlessly.")
