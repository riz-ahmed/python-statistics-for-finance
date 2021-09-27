import import_data_in_csv as f_csv
import plot_data as b_plt
import plot_profit
import cumsum_wealth
import plot_cumsum_wealth

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
fb_data['MA50'] = MovingAverage(50) # slow curve for MA10>MA50 trading strategy
fb_data['MA10'] = MovingAverage(10) # fast curve for MA10>MA50 trading strategy

# add a new column called Shares which will indicate a share BUY when MA10>MA50
fb_data['Shares'] = [1 if fb_data['MA10'].loc[ei] >
                     fb_data['MA50'].loc[ei] else 0 for ei in fb_data.index]

# add a column called Profit, profit is calculated as difference from tomorrows closing price
fb_data['Profit'] = [fb_data['Close'].shift(-1).loc[ei] - fb_data['Close'].loc[ei]
                     if fb_data['Shares'].loc[ei] == 1 else 0
                     for ei in fb_data.index]

# count the number of trades
print("No. of trades using strategy MA10 > MA50: {} and Net Profit: {}".format(
    fb_data['Shares'].sum(), fb_data['Profit'].sum()))
# b_plt.basic_plot(fb_data)
# plot_profit.plot_profit(fb_data)

# create a column to calcuate the cumsum wealth accquired with the given strategy
fb_data['Wealth'] = cumsum_wealth.cal_cumsum_wealth(fb_data)

plot_cumsum_wealth.plot_cumsum_wealth(fb_data)
