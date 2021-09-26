import pandas as pd
import matplotlib.pyplot as plt


def import_stock_csv(file):
    # import a csv data
    #file = "FB.csv"
    fb_data = pd.read_csv(file)
    # Ensure the dataframe is loaded properly
    print("Head of the data")
    print(fb_data.head())
    # print the size of the dataframe
    print("shape of the data")
    print(fb_data.shape)
    # summary of the statistics for this dataframe
    print("statistical summary of the data")
    print(fb_data.describe())

    return fb_data


def basic_plot(fb_data):
    """Pass a pd.DataFrame to this funtion, the funtion will convert the 'Date' field to
    data-time format, assign it to the current index. Which will be then used to plot
    a stocks closing at for the respective dates"""
    # change the date columns from str to date-time so as to plot the data
    fb_data['Date'] = pd.to_datetime(fb_data.Date)

    # print the close of the stocks form the imported data
    plt.figure(figsize=(10, 8))
    fb_data.set_index('Date', inplace=True)
    fb_data['Close'].plot()
    plt.show()
