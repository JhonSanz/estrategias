import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_lines_chart(data, x_label, y_label, months):
    data = data.dropna()
    x = data[x_label]
    y = data[y_label]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)  
    plt.plot(x, y, marker='.')

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=months))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%-m-%-d %H:%M'))
    fig.autofmt_xdate()
    plt.show()
