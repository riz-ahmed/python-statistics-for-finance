import matplotlib.pyplot as plt


def plot_cumsum_wealth(pd_data):
    pd_data['Wealth'].plot()
    plt.title("Money won form this Strategy is {}".format(
        pd_data['Wealth'].iloc[-2]))
    plt.show()
