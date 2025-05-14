# File: covid_tracker.ipynb

# --- Cell 1 ---
# 📦 Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Setup visual aesthetics
sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)

# --- Cell 2 ---
# 🌍 Load COVID-19 Dataset from Our World in Data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)
df.head()

# --- Cell 3 ---
# 🧹 Clean Data: Filter by countries of interest
countries = ["Kenya", "India", "United States"]
df = df[df["location"].isin(countries)]
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["location", "date"])
df = df.fillna(method="ffill")
df = df.dropna(subset=["total_cases", "total_deaths", "total_vaccinations"], how="any")
df.head()

# --- Cell 4 ---
# 📊 Total Cases Over Time
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

# --- Cell 5 ---
# 📊 Total Deaths Over Time
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.show()

# --- Cell 6 ---
# 📈 New Cases Per Day
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["new_cases"], label=country)
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.show()

# --- Cell 7 ---
# 📉 Death Rate (Total Deaths / Total Cases)
df["death_rate"] = df["total_deaths"] / df["total_cases"]
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["death_rate"], label=country)
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.show()

# --- Cell 8 ---
# 💉 Vaccination Progress
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_vaccinations"], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()

# --- Cell 9 ---
# 🗺️ Optional: Choropleth Map - Total Cases by Country (latest date)
latest = df[df["date"] == df["date"].max()]
fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Global COVID-19 Total Cases (Latest)"
                   )
fig.show()

# --- Cell 10 ---
# 📌 Summary Insights (Markdown cell)
# Use markdown in Jupyter:
'''
### 📌 Insights Summary:

- 🇺🇸 The United States consistently had the highest case count.
- 🇮🇳 India had a steep rise in mid-2021, catching up to global leaders.
- 🇰🇪 Kenya had lower total cases but a similar death rate trend.
- 💉 Vaccination uptake varied; the U.S. led in early rollout.
- 📉 Death rate trends declined as vaccinations increased.
'''
