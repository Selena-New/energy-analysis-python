import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file — this is how you will load ENTSO-E data later
df = pd.read_csv("swedish_energy.csv")

# Convert date column to proper date format
df["date"] = pd.to_datetime(df["date"])

print("=== Data loaded successfully ===")
print(f"Number of days: {len(df)}")
print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")
print()
print(df.head())
print()

# Basic analysis
print("=== Energy Production Summary ===")
print(f"Average daily solar:  {df['solar_mwh'].mean():.1f} MWh")
print(f"Average daily wind:   {df['wind_mwh'].mean():.1f} MWh")
print(f"Average electricity price: {df['price_sek_mwh'].mean():.0f} SEK/MWh")
print()

# Find the most expensive and cheapest days
expensive_day = df.loc[df["price_sek_mwh"].idxmax()]
cheap_day = df.loc[df["price_sek_mwh"].idxmin()]
print(f"Most expensive day: {expensive_day['date'].date()} at {expensive_day['price_sek_mwh']} SEK/MWh")
print(f"Cheapest day:       {cheap_day['date'].date()} at {cheap_day['price_sek_mwh']} SEK/MWh")
print()

# Plot price over time
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["price_sek_mwh"], marker="o", color="steelblue", linewidth=2)
plt.title("Swedish Electricity Price — January 2024")
plt.xlabel("Date")
plt.ylabel("Price (SEK/MWh)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("electricity_price.png")
plt.show()
print("Chart saved!")

# Reload the csv freshly for this analysis
df2 = pd.read_csv("swedish_energy.csv")

# Calculate correlation between wind production and price
correlation = df2["wind_mwh"].corr(df2["price_sek_mwh"])
print(f"\nCorrelation between wind production and price: {correlation:.2f}")

if correlation < -0.3:
    print("Result: When wind is HIGH, price tends to be LOW")
    print("This confirms the real market pattern in Sweden!")
elif correlation > 0.3:
    print("Result: Wind and price move together")
else:
    print("Result: Weak relationship in this small dataset")

# Scatter plot: wind vs price
plt.figure(figsize=(8, 5))
plt.scatter(df2["wind_mwh"], df2["price_sek_mwh"], color="steelblue", s=80)
plt.title("Wind Production vs Electricity Price")
plt.xlabel("Wind Production (MWh)")
plt.ylabel("Price (SEK/MWh)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("wind_vs_price.png")
plt.show()
print("Scatter plot saved!")