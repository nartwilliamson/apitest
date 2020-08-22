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
tickerList2 = ['QQQ', 'SPY', 'DIA', 'FXI']

ticker_history2 = client.get_dataframe(tickerList2,
                                      frequency='weekly',
                                      metric_name='adjClose',
                                      startDate='2019-11-1',
                                      endDate=Today)

testDataframe = ticker_history2.pct_change().dropna()
TempDF = testDataframe
TempDF['index2'] = testDataframe.index
testDataframe['DateColumn'] = TempDF['index2'].dt.strftime('%m-%d-%Y')
testDataframe = testDataframe.drop(['index2'], axis=1)

#stockDict.items()
stockDict = testDataframe.to_dict('records')
#columnNames = ['TSLA', 'INTC'] - this is already tickerlist2 above for dataframe API pull
tempList = []
for name in tickerList2:
    for p in stockDict:
        tempList.append({"Value" : (p[name]), "Date": p['DateColumn'], "Ticker":name})


@app.route('/')
def index():
  return "<h1>Welcome changes 1</h1>"

@app.route('/test')
def test2():
  return "<h1>test2</h1>"


@app.route('/stocks') 
def get_stores():
    return jsonify(tempList)

