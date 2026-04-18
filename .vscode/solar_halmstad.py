import pvlib
import pandas as pd
import matplotlib.pyplot as plt

# Define location — Halmstad, Sweden
latitude  = 56.67
longitude = 12.86
altitude  = 10
timezone  = "Europe/Stockholm"

# Create location object
location = pvlib.location.Location(
    latitude=latitude,
    longitude=longitude,
    tz=timezone,
    altitude=altitude,
    name="Halmstad, Sweden"
)

# Generate one year of hourly timestamps
times = pd.date_range(
    start="2024-01-01",
    end="2024-12-31 23:00",
    freq="h",
    tz=timezone
)

# Calculate solar position for every hour of the year
solar_position = location.get_solarposition(times)

# Calculate clear-sky irradiance
clearsky = location.get_clearsky(times)

print("=== Solar Analysis — Halmstad, Sweden ===")
print(f"Location: {latitude}N, {longitude}E")
print(f"Data points: {len(times)} hours (full year)")
print()
print("=== Monthly Average Solar Irradiance (W/m2) ===")
monthly = clearsky["ghi"].resample("ME").mean().round(1)
monthly.index = monthly.index.strftime("%B")
print(monthly.to_string())
print()
print(f"Best month:  {monthly.idxmax()} ({monthly.max()} W/m2)")
print(f"Worst month: {monthly.idxmin()} ({monthly.min()} W/m2)")

# Plot monthly irradiance
plt.figure(figsize=(12, 5))
monthly.plot(kind="bar", color="orange", edgecolor="darkorange")
plt.title("Monthly Average Solar Irradiance — Halmstad, Sweden (2024)")
plt.xlabel("Month")
plt.ylabel("Irradiance (W/m2)")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("solar_halmstad.png")
plt.show()
print("Chart saved as solar_halmstad.png")