import json
from flask import Flask,jsonify
import yfinance as yf
from flask_cors import CORS
# import JSON

# https://pypi.org/project/yfinance/
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stock')
def get_data():
    msft = yf.Ticker("MSFT")

# Get historical market data for the last 1 month
    hist = msft.history(period="1mo")
    ar=[]
    # Print date and closing price
    for index, row in hist.iterrows():
        date = index.strftime('%Y-%m-%d')
        closing_price = row['Close']
# 'Date': {date},
        
        ar.append({'price' :closing_price,"date":date} )

    return json.dumps(ar)


if __name__ == '__main__':
    app.run(debug=True)
