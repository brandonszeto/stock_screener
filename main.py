import matplotlib.pyplot as plt
import yfinance as yf
from filters import apply_filters

def compute_percent_returns(filtered_puts, current_price, ticker, week52_high,
                            week52_low):

    filtered_puts['Return_Percent'] = filtered_puts.apply(
        lambda x: (((x['strike'] + x['bid']) / x['strike']) * 100) - 100 if x['strike'] < current_price 
        else (((current_price + x['bid']) / x['strike']) * 100) - 100, axis=1)

    plt.figure(figsize=(10, 6))
    plt.scatter(filtered_puts['strike'], filtered_puts['Return_Percent'], color='blue')
    plt.axvline(x=current_price, color='green', linestyle='--', linewidth=1)
    plt.axvline(x=week52_high, color='red', linestyle='-.', linewidth=1, label='52-Week High')
    plt.axvline(x=week52_low, color='red', linestyle='-.', linewidth=1, label='52-Week Low')
    plt.title(f'Filtered Potential Return from Selling Puts of {ticker}')
    plt.xlabel('Strike Price ($)')
    plt.ylabel('Return (%)')
    plt.grid(True)
    plt.show()

def process_options_data(ticker):
    aapl = yf.Ticker(ticker)
    current_price = aapl.history(period="1d")['Close'].iloc[-1]
    exp_date = aapl.options[1]
    options_data = aapl.option_chain(exp_date)
    puts = options_data.puts

    hist = aapl.history(period="3mo")  # Fetch historical data for the last year
    week52_high = hist['High'].max()
    week52_low = hist['Low'].min()

    print(current_price)
    print(exp_date)

    filtered_puts = apply_filters(puts)
    compute_percent_returns(filtered_puts, current_price, ticker, week52_high, week52_low)

if __name__ == '__main__':
    process_options_data('CRWD')

