import import_data_in_csv as f_csv
import plot_data as b_plt

fb_data = f_csv.import_stock_csv('FB.csv')

# create new column in the dataframe to calculate the price diff
fb_data['PriceDiff'] = fb_data['Close'].shift(-1) - fb_data['Close']

# create a new column in the dataframe to caculate Daily Return
fb_data['Return'] = fb_data['PriceDiff'] / fb_data['Close']

# create a new column in the dataframe to calculate Direction of the stock
fb_data['Direction'] = [1 if fb_data['PriceDiff'].loc[ei]
                        > 0 else 0 for ei in fb_data.index]

# create a new column for [MA] moving average calculation


def MovingAverage(n):
    return fb_data['Close'].rolling(n).mean()


fb_data['MA200'] = MovingAverage(200)
fb_data['MA50'] = MovingAverage(50)

b_plt.basic_plot(fb_data)
