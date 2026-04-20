# Energy Data Analysis — Swedish Power Market
**MSc Renewable Energy Systems | Halmstad University**
Saghi Tayebeh Khabbaz

---

## About This Repository
Python-based energy data analysis projects using real industry data from the ENTSO-E 
Transparency Platform. This portfolio demonstrates skills in energy data engineering, 
pandas analysis, and matplotlib visualisation — tools used daily by energy analysts 
at companies like Vattenfall, E.ON, and Sweco.

---

## Project 1 — SE3 Swedish Electricity Market Analysis 2024
**File:** `python entsoe_sweden_analysis.py`  
**Data source:** ENTSO-E Transparency Platform (live API)  
**Period:** Full year 2024 | **Zone:** SE3 (Stockholm/Central Sweden)

### What this project does
Pulls a full year of hourly electricity market data directly from the ENTSO-E API 
and analyses three key variables: day-ahead prices, wind generation, and solar generation.

### Key findings
| Metric | Value |
|--------|-------|
| Average day-ahead price | 35.82 €/MWh |
| Peak price | 707.52 €/MWh (12 Dec 2024 — winter cold snap) |
| Lowest price | -59.96 €/MWh (11 Aug 2024 — renewable surplus) |
| Average wind generation | 1,148 MW |
| Average solar generation | 124 MW |

### Charts produced
| Chart | Description |
|-------|-------------|
| `se3_price_daily_2024.png` | Daily average electricity price — full year |
| `se3_price_monthly_2024.png` | Monthly average price trend |
| `se3_wind_solar_monthly_2024.png` | Wind vs solar generation by month |
| `se3_wind_vs_price_2024.png` | Scatter plot: wind generation vs price (negative correlation) |

### Insights
- **Winter peaks:** Prices spike in January and December due to heating demand and low solar
- **Summer lows:** August shows the lowest average prices (~8 €/MWh) when solar, wind, 
  and hydro all produce simultaneously
- **Negative prices:** On 11 August 2024, prices dropped to -59.96 €/MWh — 
  excess renewable generation forces the market negative
- **Wind-price correlation:** The scatter plot clearly shows that higher wind generation 
  drives lower electricity prices — a key dynamic in the Nordic power market

### Tools used
- `entsoe-py` — ENTSO-E REST API client
- `pandas` — data processing and resampling
- `matplotlib` — visualisation

---

## Project 2 — Solar Irradiance Simulation, Halmstad
**File:** `solar_halmstad.py`  
**Data source:** pvlib + SMHI weather data  
Simulates solar irradiance and energy yield for Halmstad, Sweden.

---

## Setup
```bash
pip install entsoe-py pandas matplotlib
```
Add your ENTSO-E API token (register free at transparency.entsoe.eu):
```python
API_KEY = 'your-token-here'
```

---

