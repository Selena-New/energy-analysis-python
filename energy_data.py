import pandas as pd

# Weekly solar production data (kWh) - a small Swedish solar system
data = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "solar_kwh": [12.5, 18.3, 9.1, 22.7, 15.4, 28.9, 24.1],
    "wind_kwh":  [45.2, 38.7, 52.1, 31.4, 48.6, 22.3, 35.8]
}

# Create a DataFrame - the core tool of energy data analysis
df = pd.DataFrame(data)

print("=== Weekly Energy Production ===")
print(df)
print()
print("=== Summary Statistics ===")
print(df[["solar_kwh", "wind_kwh"]].describe().round(2))
print()
print(f"Total solar this week:  {df['solar_kwh'].sum():.1f} kWh")
print(f"Total wind this week:   {df['wind_kwh'].sum():.1f} kWh")
print(f"Best solar day: {df.loc[df['solar_kwh'].idxmax(), 'day']}")
print(f"Best wind day:  {df.loc[df['wind_kwh'].idxmax(), 'day']}")

import matplotlib.pyplot as plt

# Create a bar chart of solar vs wind production
df.plot(x="day", y=["solar_kwh", "wind_kwh"], kind="bar", figsize=(10, 5))
plt.title("Weekly Solar and Wind Production - Halmstad")
plt.xlabel("Day")
plt.ylabel("Energy (kWh)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weekly_energy.png")
plt.show()
print("Chart saved as weekly_energy.png")