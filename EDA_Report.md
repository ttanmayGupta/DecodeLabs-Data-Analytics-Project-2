# EDA Report - DecodeLabs Project 2

## 1. Introduction
This project performs Exploratory Data Analysis (EDA) on a sample sales dataset.
The purpose is to understand the dataset through descriptive statistics, trends,
outlier detection and visualizations.

## 2. Dataset
The dataset contains 48 sales records with these columns:
- Date
- Product
- Category
- Quantity
- Sales
- Profit

## 3. Basic Statistics

| Metric | Quantity | Sales | Profit |
|---|---:|---:|---:|
| Count | 48 | 48 | 48 |
| Mean | 17.60 | ₹433,059.97 | ₹71,021.63 |
| Median | 15.00 | ₹347,924.23 | ₹56,791.85 |

## 4. Trend Analysis
The highest monthly sales occurred in **2026-01**, with total sales of
**₹1,600,868.39**.

The lowest monthly sales occurred in **2027-03**, with total sales of
**₹13,644.22**.

The monthly-sales graph is used to visualize the movement of sales over time.

## 5. Outlier Detection
The IQR method was used.

- Q1: ₹96,769.02
- Q3: ₹647,957.21
- IQR: ₹551,188.19
- Lower bound: ₹-730,013.27
- Upper bound: ₹1,474,739.50
- Number of detected outliers: **1**

The outlier is unusually high compared with most sales records and should be
investigated rather than automatically deleted.

## 6. Category Analysis
The highest total sales came from **Electronics**.

## 7. Key Observations
1. The dataset contains 48 records.
2. Average sales are ₹433,059.97, while median sales are ₹347,924.23.
3. The difference between mean and median is influenced by unusually large sales values.
4. A clear high-value sales outlier was detected using the IQR method.
5. Monthly grouping helps identify the highest and lowest sales periods.
6. Visualizations make the sales trend and relationships easier to understand.

## 8. Conclusion
EDA converted the raw sales table into meaningful information by calculating
basic statistics, identifying a time trend, detecting outliers and visualizing
important relationships. The analysis demonstrates the core requirements of
DecodeLabs Project 2.
