import pandas as pd
import matplotlib.pyplot as plt


def basic_plot(fb_data):
    """Pass a pd.DataFrame to this funtion, the funtion will convert the 'Date' field to
    data-time format, assign it to the current index. Which will be then used to plot
    a stocks closing at for the respective dates"""
    # change the date columns from str to date-time so as to plot the data
    fb_data['Date'] = pd.to_datetime(fb_data.Date)

    # print the close of the stocks form the imported data
    plt.figure(figsize=(10, 8))
    fb_data.set_index('Date', inplace=True)
    fb_data['MA200'].plot(label='MA200')
    fb_data['MA50'].plot(label='MA50')
    fb_data['MA10'].plot(label='MA10')
    fb_data['Close'].plot(label='Close')
    plt.legend()
    plt.show()
