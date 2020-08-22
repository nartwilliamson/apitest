from flask import Flask






app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Welcome changes 1</h1>"

@app.route('/test')
def test2():
  return "<h1>test2</h1>"


