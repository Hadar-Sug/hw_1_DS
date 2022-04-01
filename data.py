import pandas
import numpy as np
import statistics as stat


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    features = string_to_array(features)
    return dict((k, data[k]) for k in features if k in data)


def num_of_row(feature, data):
    for k in range(5):
        if data[k][0] == feature:
            return k


def matrix_to_dict(matrix, data):
    dictionary = dict()
    for index, item in enumerate(data):
        feature = item[0]
        row = np.array(matrix[index, :])
        dictionary[feature] = row
    return dictionary


def string_to_array(string):
    return string.split(',')


def filter_by_feature(data, feature, value):
    data_all = np.array([data[k][1] for k in range(5)])
    data1 = np.array([])
    data2 = np.array([])
    row = num_of_row(feature, data)
    for column in range(data_all.shape[1]):
        current = data_all[row][column]
        if current == value:
            data1 = np.block([[data1, data_all[:, column]]])
        else:
            data2 = np.block([[data1, data_all[:, column]]])
    return matrix_to_dict(data1, data), matrix_to_dict(data2, data)


# need to change functions to for loops
def print_details(data, features, statistic_functions):
    for feature in features:
        print("{}: ".format(feature))
        for i, func in enumerate(statistic_functions):
            func_val = statistic_functions[i](data[feature])
            print("{}".format(func_val))
            if i != len(statistic_functions):
                print(", ")
            else:
                print("\n")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    feature1 = data[features[0]]
    feature2 = data[features[1]]
    for i, func in enumerate(statistic_functions):
        method_name = statistic_functions_names[i]
        function = statistic_functions[i](feature1, feature2)
        print("{}({}, {}): {}".format(method_name, features[0], features[1], function))


def filter_by_feature_hadar(data, feature, value):
    true_dict = {}
    false_dict = {}
    for k, v in data:
        true_list = []
        false_list = []
        for a, wanted in zip(v, data[feature].values()):
            if wanted == value:
                true_list.append(a)
            else:
                false_list.append(a)
        true_dict[k] = true_list
        false_dict[k] = false_list
    return true_dict, false_dict
