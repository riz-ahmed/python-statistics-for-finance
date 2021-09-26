import pandas as pd
import matplotlib.pyplot as plt
import import_data_in_csv as f_csv

fb_data = f_csv.import_stock_csv('FB.csv')
f_csv.basic_plot(fb_data)
