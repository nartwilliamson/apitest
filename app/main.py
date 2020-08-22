from flask import Flask, jsonify, request



from tiingo import TiingoClient
import numpy as np
import pandas as pd


app = Flask(__name__)


config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = "a5e87637752491cca8c3a282688dbe81f7243561"

#quandl uUfmVoEksfwWxMA4tQcd
# Initialize
client = TiingoClient(config)


Today = pd.datetime.today().strftime("%Y/%m/%d") 
tickerList = ['TSLA', 'QQQ']


ticker_history = client.get_dataframe(tickerList,
                                      frequency='weekly',
                                      metric_name='adjClose',
                                      startDate='2019-10-01',
                                      endDate=Today)


ticker_history['index2'] = ticker_history.index
ticker_history['date'] = ticker_history['index2'].dt.strftime('%Y-%m-%d')
stockData = ticker_history.to_json(orient='records', date_format='none')


@app.route('/')
def index():
  return "<h1>Welcome changes 1</h1>"

@app.route('/test')
def test2():
  return "<h1>test2</h1>"


@app.route('/stocks') 
def get_stores():
    return stockData


