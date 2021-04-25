import copy
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graphics(abscissa, ordinate, ylabl, xlabl, text):
    x = copy.deepcopy(abscissa)
    y = copy.deepcopy(ordinate)
    if ylabl == 'neutron_glob14' or ylabl == 'neutron_glob12':
        for i in range(len(y)):
            y[i] = y[i] / 1000
        text = ylabl + ', $10^3$'
    plt.figure(figsize=(13, 7))
    sns.set_theme()
    plt.plot(x, y)
    plt.xlabel(xlabl)
    plt.ylabel(ylabl)
    plt.savefig(text + '.jpg')
    plt.show()
    return
