
import pandas as pd


def import_stock_csv(file):
    # import a csv data
    #file = "FB.csv"
    fb_data = pd.read_csv(file)
    # Ensure the dataframe is loaded properly
    # print("Head of the data")
    # print(fb_data.head())
    # # print the size of the dataframe
    # print("shape of the data")
    # print(fb_data.shape)
    # # summary of the statistics for this dataframe
    # print("statistical summary of the data")
    # print(fb_data.describe())

    return fb_data
