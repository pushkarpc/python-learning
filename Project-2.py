from alpha_vantage.timeseries import TimeSeries

# opening text file with the API key
with open("alpha_vantage_api.txt") as file:
    API_KEY = file.read().strip()

print(API_KEY)
# install alpha_vantage python package

#building the TimeSeries variable from Alpha Vantage API
timeSeries1 = TimeSeries(key= API_KEY)

#get monthly stock data of Apple
print(timeSeries1.get_monthly("AAPL"))
