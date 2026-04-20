from entsoe import EntsoePandasClient
import pandas as pd

client = EntsoePandasClient(api_key='2417a8de-84c5-4231-ab64-dc1726213d44')

start = pd.Timestamp('2024-01-01', tz='Europe/Stockholm')
end   = pd.Timestamp('2024-01-07', tz='Europe/Stockholm')

prices = client.query_day_ahead_prices('SE_3', start=start, end=end)
print(prices)