from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup

# opening text file with the API key
with open("alpha_vantage_api.txt") as file:
    API_KEY = file.read().strip()

print(API_KEY)
# install alpha_vantage python package

#building the TimeSeries variable from Alpha Vantage API
timeSeries1 = TimeSeries(key= API_KEY)

#getting monthly stock data of Apple
print(timeSeries1.get_monthly("AAPL"))

#getting monthly stock data of Apple with string concatenation of API key
url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=" + str(API_KEY)
r = requests.get(url)
data = r.json()
print(data)

#getting weekly stock data of Apple and applying BeautifulSoup
url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=AAPL&apikey=" + str(API_KEY)
r = requests.get(url)
data = BeautifulSoup(r.content)
print(data)

#getting intraday stock data of Apple
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=60min&apikey=" + str(API_KEY)
r = requests.get(url)
data = BeautifulSoup(r.content)
print(data)