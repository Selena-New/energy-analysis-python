# ============================================================
# Month 1 Portfolio Project — Swedish Energy Data Analysis
# ENTSO-E Transparency Platform + pandas + matplotlib
# Saghi Tayebeh Khabbaz
# ============================================================

from entsoe import EntsoePandasClient
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Configuration ---
API_KEY = '2417a8de-84c5-4231-ab64-dc1726213d44'  # Replace with new token if regenerated
ZONE    = 'SE_3'
START   = pd.Timestamp('2024-01-01', tz='Europe/Stockholm')
END     = pd.Timestamp('2024-12-31', tz='Europe/Stockholm')

client = EntsoePandasClient(api_key=API_KEY)

print("Fetching data from ENTSO-E... this may take 30-60 seconds.")

# ============================================================
# 1. PULL DATA
# ============================================================

# Day-ahead electricity prices (€/MWh)
prices = client.query_day_ahead_prices(ZONE, start=START, end=END)

# Wind generation (MW)
wind = client.query_wind_and_solar_production(ZONE, start=START, end=END)['Wind Onshore']

# Solar generation (MW)
solar = client.query_wind_and_solar_production(ZONE, start=START, end=END)['Solar']

print("Data fetched successfully!")
print(f"  Prices: {len(prices)} hourly records")
print(f"  Wind:   {len(wind)} hourly records")
print(f"  Solar:  {len(solar)} hourly records")

# ============================================================
# 2. PANDAS ANALYSIS
# ============================================================

# --- Daily averages ---
prices_daily = prices.resample('D').mean()
wind_daily   = wind.resample('D').mean()
solar_daily  = solar.resample('D').mean()

# --- Weekly peaks ---
prices_weekly_peak = prices.resample('W').max()
wind_weekly_peak   = wind.resample('W').max()

# --- Monthly trends ---
prices_monthly = prices.resample('ME').mean()
wind_monthly   = wind.resample('ME').mean()
solar_monthly  = solar.resample('ME').mean()

# --- Summary statistics ---
print("\n--- SUMMARY STATISTICS 2024 ---")
print(f"Average price:      {prices.mean():.2f} €/MWh")
print(f"Peak price:         {prices.max():.2f} €/MWh  on {prices.idxmax().date()}")
print(f"Lowest price:       {prices.min():.2f} €/MWh  on {prices.idxmin().date()}")
print(f"Average wind:       {wind.mean():.0f} MW")
print(f"Average solar:      {solar.mean():.0f} MW")

# ============================================================
# 3. PLOTS
# ============================================================

os.makedirs('output', exist_ok=True)

# --- Plot 1: Monthly average electricity price ---
fig, ax = plt.subplots(figsize=(12, 5))
prices_monthly.plot(ax=ax, color='steelblue', linewidth=2, marker='o')
ax.set_title('SE3 Monthly Average Day-Ahead Price — 2024', fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Price (€/MWh)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/se3_price_monthly_2024.png', dpi=150)
print("\nSaved: output/se3_price_monthly_2024.png")

# --- Plot 2: Monthly wind vs solar generation ---
fig, ax = plt.subplots(figsize=(12, 5))
wind_monthly.plot(ax=ax, label='Wind Onshore', color='royalblue', linewidth=2, marker='o')
solar_monthly.plot(ax=ax, label='Solar', color='orange', linewidth=2, marker='s')
ax.set_title('SE3 Monthly Average Wind & Solar Generation — 2024', fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Generation (MW)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/se3_wind_solar_monthly_2024.png', dpi=150)
print("Saved: output/se3_wind_solar_monthly_2024.png")

# --- Plot 3: Daily price — full year ---
fig, ax = plt.subplots(figsize=(14, 5))
prices_daily.plot(ax=ax, color='steelblue', linewidth=1)
ax.set_title('SE3 Daily Average Electricity Price — 2024', fontsize=14)
ax.set_xlabel('Date')
ax.set_ylabel('Price (€/MWh)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/se3_price_daily_2024.png', dpi=150)
print("Saved: output/se3_price_daily_2024.png")

# --- Plot 4: Price vs Wind correlation ---
combined = pd.DataFrame({'Price (€/MWh)': prices_daily, 'Wind (MW)': wind_daily}).dropna()
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(combined['Wind (MW)'], combined['Price (€/MWh)'],
           alpha=0.4, color='steelblue', edgecolors='white', s=30)
ax.set_title('SE3 Wind Generation vs Day-Ahead Price — 2024', fontsize=13)
ax.set_xlabel('Average Daily Wind Generation (MW)')
ax.set_ylabel('Average Daily Price (€/MWh)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/se3_wind_vs_price_2024.png', dpi=150)
print("Saved: output/se3_wind_vs_price_2024.png")

# --- Save to CSV ---
combined.to_csv('output/se3_daily_summary_2024.csv')
print("Saved: output/se3_daily_summary_2024.csv")

print("\n✅ Analysis complete! Check the 'output' folder.")