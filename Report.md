Weather Data Analysis & Visualization Report

Course: Programming for Problem Solving using Python
Assignment: Lab Assignment 4 — Weather Data Visualizer
Student: Manthan Sharma
Roll No.: 2501410037

1. Introduction

Weather patterns play a major role in everyday life, and analyzing them gives us a better understanding of seasonal changes and climate behavior.
In this assignment, I worked with a real-world weather dataset, cleaned it, performed statistical analysis, created visualizations, and extracted meaningful insights using Python. The main focus was on temperature, humidity, rainfall, and date-based grouping.

2. Dataset Overview

The raw dataset (weather.csv) contained 20 different weather-related columns collected over many years. Some important fields relevant to this assignment were:

datetime_utc (timestamp)
_tempm (temperature in Celsius)
_hum (humidity percentage)
_rain (rain indicator, 0 or 1)

The dataset had several issues, such as:

Leading spaces in column names
Missing values
Invalid values like -9999
Irregular date formatting
After cleaning and preprocessing the data, four main columns were kept:
date, temperature, humidity, rainfall

This simplified dataset was used for all analysis and plotting.

3. Data Cleaning Steps

The data cleaning process was essential to make the dataset usable. The following operations were performed:

Removed whitespace from all column names
Renamed the main weather-related columns
Replaced invalid values such as -9999
Removed rows with missing temperature, humidity, or rainfall values
Converted the date column to proper datetime format
Dropped all corrupt or unusable entries
Saved the cleaned dataset as cleaned_weather.csv

This produced a consistent and reliable dataset for further analysis.

4. Statistical Summary

Using Pandas and NumPy, several temperature-related statistics were calculated:

Average Temperature: 25.45°C
Minimum Temperature: 1°C
Maximum Temperature: 90°C
Standard Deviation: 8.48°C

These figures indicate clear seasonal variations in temperature, ranging from winter lows to extreme summer highs.

5. Visualizations

Three visualizations were created using Matplotlib to better understand weather trends.

5.1 Daily Temperature Trend (Line Chart)

This chart shows temperature changes across different days.
The pattern indicates warming trends during summer months and cooling trends during winter.

Saved as: temp_trend.png

5.2 Monthly Rainfall Totals (Bar Chart)

Since the dataset includes a rain indicator (0 or 1), monthly rainfall totals were calculated by summing the rain values.

Observations:

Rainfall is heavily concentrated in the monsoon months (June to September)
Winter and early spring have low or almost no rainfall

Saved as: monthly_rain.png

5.3 Humidity vs Temperature (Scatter Plot)

This plot helps identify the relationship between humidity and temperature.

Observations:

Higher humidity values appear mostly during monsoon months
Dry and hot months show lower humidity
The relationship varies seasonally

Saved as: humid_temp_scatter.png

6. Grouping and Aggregation Analysis

The dataset was grouped by month to calculate:

Average temperature
Total rainfall
Average humidity

This monthly breakdown clearly highlights seasonal patterns:

Summer (April to June): High temperatures
Monsoon (July to September): High rainfall and high humidity
Winter (December to January): Lowest temperatures

This grouping helps understand how weather behavior changes across the year.

7. Insights and Interpretation

After analyzing the cleaned data, the following insights were drawn:

Temperature follows a predictable seasonal cycle, with clear peaks in summer and lows in winter.
Rainfall sharply increases during monsoon months, which also raises humidity levels.
Humidity levels drop significantly during dry summer months.

Despite initial noise and missing values, the cleaned dataset shows consistent and reliable trends.

8. Conclusion

This assignment helped in understanding how real-world weather data can be cleaned, processed, and analyzed using Python.
Key learnings included:

Working with Pandas for data cleaning
Using NumPy for statistical computation
Creating visualizations with Matplotlib
Applying grouping and aggregation techniques
Extracting meaningful insights from raw, messy data

The project successfully demonstrates the full workflow of data analysis, from raw input to processed insights.

9. Files Included

weather_visualizer.py — Python script

weather.csv — Raw dataset
cleaned_weather.csv — Cleaned dataset
temp_trend.png — Temperature line chart
monthly_rain.png — Rainfall bar chart
humid_temp_scatter.png — Humidity vs temperature scatter plot

README.md — Screenshots of Project Output 

Report.md — This report
