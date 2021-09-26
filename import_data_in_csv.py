import pandas as pd
import matplotlib.pyplot as plt

# import a csv data
file = "FB.csv"
fb_data = pd.read_csv(file)
# Ensure the dataframe is loaded properly
print(fb_data.head())
# print the size of the dataframe
print(fb_data.shape)
# summary of the statistics for this dataframe
print(fb_data.describe())

# change the date columns from str to date-time so as to plot the data
fb_data['Date'] = pd.to_datetime(fb_data.Date)

# print the close of the stocks form the imported data
plt.figure(figsize=(10, 8))
fb_data.set_index('Date', inplace=True)
fb_data['Close'].plot()
plt.show()
