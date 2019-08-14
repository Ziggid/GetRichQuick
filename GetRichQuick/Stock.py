import requests


def getCurrentStockPrice(stockId: str):
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stockId +
        "&interval=1min&outputsize=compact&apikey=HUTM7V18LBLQPIOP")

    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)

    # The service sends JSON data, we parse that into a Python datastructure
    raw_data = response.json()
    return [max(raw_data['Time Series (1min)'].keys()),
            raw_data['Time Series (1min)'][max(raw_data['Time Series (1min)'].keys())]['4. close']]
