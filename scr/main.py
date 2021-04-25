from Reader import reader, make_arrays
from visualization import plot_graphics
from scr.algorithms import correlation_function, normalization

if __name__ == '__main__':
    data = reader("../data/21022518.txt")
    arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12 = make_arrays(data)
    plot_graphics(arr9, arr12, 'plasma_pos', 't, мс', 'plasma_pos')
    plot_graphics(arr9, arr8, 'neutron_glob14', 't, мс', 'neutron_glob14')
    plot_graphics(arr9, arr10, 'neutron_glob12', 't, мс', 'neutron_glob12')
    tau, corr = correlation_function(arr8, arr12)
    plot_graphics(tau, corr, 'corr_func', 'tau', 'corr_14')
    corr = normalization(corr)
    plot_graphics(tau, corr, 'norm_corr_func', 'tau', 'n_corr_14')

    tau, corr = correlation_function(arr10, arr12)
    plot_graphics(tau, corr, 'corr_func', 'tau', 'corr_12')
    corr = normalization(corr)
    plot_graphics(tau, corr, 'norm_corr_func', 'tau', 'n_corr_12')
    tau, corr = correlation_function(arr8, arr10)


