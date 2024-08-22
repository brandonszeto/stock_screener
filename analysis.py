import matplotlib.pyplot as plt
import yfinance as yf

# Fetch the options data
aapl = yf.Ticker("AAPL")
exp_date = aapl.options[0]
options_data = aapl.option_chain(exp_date)
calls = options_data.calls
puts = options_data.puts

def plot_bid_ask_side_by_side(calls, puts):
    # Set up the figure and axes for side-by-side plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

    # Plot call options on the first subplot
    axes[0].scatter(calls['strike'], calls['bid'], alpha=0.75, color='blue', label='Bid Price')
    axes[0].scatter(calls['strike'], calls['ask'], alpha=0.75, color='green', label='Ask Price')
    axes[0].set_title('AAPL Call Options - Strike vs Price')
    axes[0].set_xlabel('Strike Price')
    axes[0].set_ylabel('Price')
    axes[0].grid(True)
    axes[0].legend()

    # Plot put options on the second subplot
    axes[1].scatter(puts['strike'], puts['bid'], alpha=0.75, color='red', label='Bid Price')
    axes[1].scatter(puts['strike'], puts['ask'], alpha=0.75, color='orange', label='Ask Price')
    axes[1].set_title('AAPL Put Options - Strike vs Price')
    axes[1].set_xlabel('Strike Price')
    axes[1].set_ylabel('Price')
    axes[1].grid(True)
    axes[1].legend()

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Call the function to plot data
plot_bid_ask_side_by_side(calls, puts)

