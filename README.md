# FUTURE_DS_02
Customer Retention &amp; Churn Analysis
# Corporate Data Analytics Case Study: Subscriber Retention & Churn Diagnostic Audit

## 📋 Executive Project Context
This repository contains an end-to-end customer intelligence and behavioral analytics pipeline built to audit historical subscriber accounts for a multi-national subscription provider using the framework of the `WA_Fn-UseC_-Telco-Customer-Churn.csv` dataset.

In subscription-based economic models (SaaS, Fintech, and Telecom), keeping an existing user is significantly more cost-effective than marketing to acquire a new one. The primary objective of this diagnostic audit was to design a data-driven system to identify high-risk churn vectors, isolate attrition drivers across key customer segments, map account tenure trends, and deliver practical strategic recommendations to maximize Customer Lifetime Value (LTV).

---

## 📊 Core Attrition Metrics (Post-Audit)
Following structural validation and metrics extraction across our account base, the company's global subscriber standing is confirmed as follows:
* **Global Customer Base Audited:** `7,032 active accounts`
* **Calculated Benchmark Churn Rate:** `26.58%`
* **Calculated Account Retention Rate:** `73.42%`
* **Average Customer Active Lifecycle:** `32.4 Months`
* **Immediate Monthly Revenue At Risk:** `$139,130.85` *(Sum of Monthly Charges from churning accounts)*

---

## 🛠️ Data Governance & Preparation Pipeline
To preserve analytical fidelity and prevent mathematical skewing before running calculations, the data was processed through a systematic cleaning sequence via our python engine (`analysis.py`):
1. **White-Space Handling:** Discovered and handled latent blank string values masquerading as data lines within the `TotalCharges` metric. 
2. **Type Enforcement:** Coerced text fields into a numeric vector (`float64`) to calculate monetary aggregates.
3. **Inception Filtering:** Isolated and removed **11 accounts** showing `NaN` data points. These represented brand new accounts with zero months of tenure where billing cycles had not yet initialized.
4. **Vector Transformation:** Mapped text flags (`Yes` / `No`) into binary analytical variables (`1` / `0`) to allow for probability groupings.

---

## 🧠 High-Impact Retention Insights

### 1. Contract Structure Architecture Risk
* **The Month-to-Month Trap:** Accounts operating on a standard Month-to-month plan exhibit an overwhelming churn rate of **42.71%**. 
* **The Long-Term Lock:** In stark contrast, customers signed to stable **One-Year (11.28% churn)** or **Two-Year (2.85% churn)** contract terms represent the most reliable structural pillars of the business. Contract structure is the single largest predictor of user attrition.

### 2. The Onboarding Attrition Wall (Lifecycle Density)
* Evaluation of customer lifetime tenure distributions shows a massive drop-off spike concentrated heavily within the **first 1 to 5 months** of subscription configuration. 
* Once an account successfully clears the 12-month onboarding threshold, their probability of churn drops dramatically, and retention levels flatline into highly predictable, long-term brand advocacy.

### 3. Payment Processing Friction & Infrastructure Vectors
* Subscribers utilizing **Electronic Checks** as their core clearing method show a severely elevated churn velocity compared to automated alternatives. 
* This signals clear operational friction, likely driven by high transactional failure rates, expired payment cards, or regular manual payment oversights, leading to involuntary churn.

---

## 📈 Strategic Recommendations for Management

* **Convert Month-to-Month Users via Incentives:** Launch an immediate account migration campaign offering a targeted discount (e.g., "Get 2 Months Free") to incentivize high-risk month-to-month subscribers to transition into stable 1-year contracts.
* **Overhaul the First-90-Days Onboarding Journey:** Since customer loss is heavily front-loaded in months 1–5, deploy dedicated retention triggers, automated setup tooltips, and proactive customer success touchpoints during the first 60 days to guide new users past the initial churn wall.
* **Enforce Automated Billing Implementations:** Systematically de-emphasize manual Electronic Check payment options. Introduce minor billing credits or loyalty points for accounts that activate **Auto-Pay via Credit Card or Direct Bank Transfer** to structurally mitigate involuntary churn.
