import matplotlib.pyplot as plt


def plot_profit(pd_data):
    pd_data['Profit'].plot()
    plt.axhline(y=0, color='red')
    plt.show()
