NUMBER_OF_PARAMETERS = 12


def reader(filename, num_of_unnecessary=4):
    data = []
    with open(filename, "r") as f:
        for line in range(num_of_unnecessary):
            f.readline()
        for line in f.readlines():
            delete_of_excess = line.replace("   ", " ")
            delete_of_excess = delete_of_excess.replace("    ", " ")
            delete_of_excess = delete_of_excess.replace("---------", "NaN")
            delete_of_excess = delete_of_excess.replace("\n", " ")
            data.append(delete_of_excess.split(" "))
    data = [list(filter(None, lst)) for lst in data]
    data = conversion_to_double(data)
    return data


def conversion_to_double(line):
    data_float_format = []
    for item in line:
        data_float_format.append([float(x) for x in item])
    return data_float_format


def make_arrays(data):
    arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12 = [], [], [], [], [], [], [], [], [], [], [], []
    for i in range(len(data)):
        for j in range(NUMBER_OF_PARAMETERS):
            if j == 0:
                arr1.append(data[i][j])
            elif j == 1:
                arr2.append(data[i][j])
            elif j == 2:
                arr3.append(data[i][j])
            elif j == 3:
                arr4.append(data[i][j])
            elif j == 4:
                arr5.append(data[i][j])
            elif j == 5:
                arr6.append(data[i][j])
            elif j == 6:
                arr7.append(data[i][j])
            elif j == 7:
                arr8.append(data[i][j])
            elif j == 8:
                arr9.append(data[i][j])
            elif j == 9:
                arr10.append(data[i][j])
            elif j == 10:
                arr11.append(data[i][j])
            else:
                arr12.append(data[i][j])
    return arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12
