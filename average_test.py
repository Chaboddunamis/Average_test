
def calculate_average_price(filename, symbol):
    df = pd.read_csv(filename)
    symbol_data = df[df['Symbol'] == symbol]
    average_price = symbol_data['Close'].mean()
    return average_price

print(calculate_average_price('stocks.csv', 'AAPL'))