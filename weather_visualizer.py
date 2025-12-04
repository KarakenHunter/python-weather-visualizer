import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
def load_data(path):
    df = pd.read_csv(path)
    print(df.head())
    print(df.info())
    print(df.describe())
    return df
    
def clean(df):
    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        "datetime_utc": "date",
        "_tempm": "temperature",
        "_hum": "humidity",
        "_rain": "rainfall"   
    })

    print("COLUMNS AFTER FIX:", df.columns)

    # clean weird values
    df["temperature"] = df["temperature"].replace(-9999, np.nan)
    df["humidity"] = df["humidity"].replace(-9999, np.nan)
    df["rainfall"] = df["rainfall"].replace(-9999, np.nan)

    df = df.dropna(subset=["temperature", "humidity", "rainfall"])

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    df = df[["date", "temperature", "humidity", "rainfall"]]

    return df
def stats(df):
    st = {}
    st["avg_temp"] = df["temperature"].mean()
    st["min_temp"] = df["temperature"].min()
    st["max_temp"] = df["temperature"].max()
    st["std_temp"] = df["temperature"].std()
    return st

def make_plots(df):
    plt.figure(figsize=(10,4))
    plt.plot(df["date"], df["temperature"])
    plt.title("Daily Temp Trend")
    plt.xlabel("date")
    plt.ylabel("temp")
    plt.tight_layout()
    plt.savefig("temp_trend.png")

    df["month"] = df["date"].dt.month
    m_rain = df.groupby("month")["rainfall"].sum()

    plt.figure(figsize=(8,4))
    m_rain.plot(kind="bar")
    plt.title("Monthly Rainfall")
    plt.xlabel("month")
    plt.ylabel("rain")
    plt.tight_layout()
    plt.savefig("monthly_rain.png")

    plt.figure(figsize=(6,4))
    plt.scatter(df["temperature"], df["humidity"])
    plt.title("Humidity vs Temp")
    plt.xlabel("temp")
    plt.ylabel("humidity")
    plt.tight_layout()
    plt.savefig("humid_temp_scatter.png")

def month_grp(df):
    df["month"] = df["date"].dt.month
    g = df.groupby("month").agg({
        "temperature": "mean",
        "rainfall": "sum",
        "humidity": "mean"
    })
    return g

def export_csv(df):
    df.to_csv("cleaned_weather.csv", index=False)


if __name__ == "__main__":
    path = "weather.csv"   
    d = load_data(path)
    d = clean(d)
    export_csv(d)
    print(stats(d))
    make_plots(d)
    print(month_grp(d))
    print("done.")
