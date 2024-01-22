import yfinance as yf

msft = yf.Ticker("MSFT")

# Get historical market data for the last 1 month
hist = msft.history(period="1mo")

# Print date and closing price
for index, row in hist.iterrows():
    date = index.strftime('%Y-%m-%d')
    closing_price = row['Close']
    print(f"Date: {date},Price: {closing_price}")