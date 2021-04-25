import copy


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


def make_tau_list():
    tau = list(range(-500, 500))
    return tau


def make_new_list(lst, steps):
    new_lst = copy.deepcopy(lst)
    shift(new_lst, steps)
    return new_lst


def count_sum(lst1, lst2):
    summary = 0
    for i in range(len(lst1)):
        summary += lst1[i] * lst2[i]
    return summary


def isNaN(num):
    return num != num


def delete_nan(lst1, lst2):
    new_lst1 = copy.deepcopy(lst1)
    new_lst2 = copy.deepcopy(lst2)
    for i in range(len(new_lst1)):
        if isNaN(new_lst1[i]):
            new_lst1[i] = 0
        if isNaN(new_lst2[i]):
            new_lst2[i] = 0
    return new_lst1, new_lst2


def correlation_function(lst1, lst2):
    corr = []
    tau = make_tau_list()
    new_lst1, new_lst2 = delete_nan(lst1, lst2)
    for step in tau:
        new_lst = make_new_list(new_lst2, step)
        corr.append(count_sum(new_lst1, new_lst))
    return tau, corr


def normalization(corr):
    norm_corr = []
    min_elem = min(corr)
    max_elem = max(corr)
    for i in range(len(corr)):
        norm_corr.append((corr[i] - min_elem) / (max_elem - min_elem))
    return norm_corr

