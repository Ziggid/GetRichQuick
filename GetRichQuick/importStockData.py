# pip install alpha_vantage
# pip install pandas
# pip install matplotlib

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import requests

class StockData:
    names = {"MSFT", "PDD", "TSE:TD", "QCOM", "DAX", "^AEX", "ING"}

    def get_current_stock_data(self, name):
        API_URL = "https://www.alphavantage.co/query"

        data = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": name,
            "interval":'1min',
            "outputsize": "compact",
            "datatype": "pandas",
            "apikey": "HUTM7V18LBLQPIOP"
        }

        print(data)
        stockdata = requests.get(API_URL, data)
        a = stockdata.json()['Time Series (1min)']
        dates = a.keys()
        date = list(dates)[0]
        return {date, a[date]['4. close']}


x = StockData()
print(x.get_current_stock_data("^AEX"))
