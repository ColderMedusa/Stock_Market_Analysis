import requests  
from config import logger, headers, url


def connect_to_api():
  stocks = ['TSLA', 'MSFT', 'GOOGL']

  json_response = []

  for stock in stocks:                      # iterate directly over the list
    querystring = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock,
        "outputsize": "compact",
        "interval": "5min",
        "datatype": "json",
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Stock {stock} loaded successfully")
        json_response.append(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error on stock {stock}: {e}")
        # either skip the rest of this iteration…
        # continue
        # …or stop the loop entirely:
        break

  return json_response  



def extract_json(response):
  records = []

  for data in response:
    symbol = data['Meta Data']['2. Symbol']

    for date_str, metrics in data['Time Series (5min)'].items():
      record = {
        "symbol": symbol,
        "date": date_str,
        "open": metrics["1. open"],
        "close": metrics["4. close"],
        "high": metrics["2. high"],
        "low": metrics["3. low"]
      }

      records.append(record)
      
  return records