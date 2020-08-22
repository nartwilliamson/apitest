from flask import Flask

from flask import Flask, jsonify

from tiingo import TiingoClient
import numpy as np
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Welcome to CodingX</h1>"


@app.route('/DOW')
def getDow():
  return "<h1>Getting DOW</h1>"