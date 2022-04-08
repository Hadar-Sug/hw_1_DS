import pandas
import numpy as np
import statistics as stat


def load_data(path, features):
    """
    forming a dictionary of the data
    :param path: path to the data
    :param features: guidelines features in data
    :return: dictionary of the dataframe
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    features = string_to_array(features)
    return dict((k, data[k]) for k in features if k in data)


def num_of_row(feature, data):
    """
    finds the row of feature
    :param feature: the feature we want the row of
    :param data: the dataframe
    :return: num of row
    """
    for k in range(5):
        if data[k][0] == feature:
            return k


def matrix_to_dict(matrix, data):
    """
    forming a dictionary from a given matrix
    :param matrix: data including matrix
    :param data: the data
    :return: the dataframe
    """
    dictionary = dict()
    for index, item in enumerate(data):
        feature = item[0]
        row = np.array(matrix[index, :])
        dictionary[feature] = row
    return dictionary


def string_to_array(string):
    """
    getting rid of commas
    :param string: sting were filtering
    :return: returns said string as an array without commas
    """
    return string.split(',')


def filter_by_feature(data, feature, value):
    """
    gets a dictionary, splits it based on a categorical value, to 2 dictionaries
    :param data: the dataframe
    :param feature: the categorical feature
    :param value: value of feature, based on this value we split the dict
    :return:
    data1 is a dictionary with values that correspond to value
    data2 is another dict with the rest
    """
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
    """
    prints statistic measures about the dataframe acc to features, using statistics.py methods
    :param data: the data frame
    :param features: the wanted features to base on
    :param statistic_functions: a list concluding statistic methods
    """
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
    """
    prints statistic measures about the dataframe, only based on features
    :param data: the dataframe
    :param features: the features were calculating according to
    :param statistic_functions: list of statistic functions
    :param statistic_functions_names: list of the names of the functions
    """
    feature1 = data[features[0]]
    feature2 = data[features[1]]
    for i, func in enumerate(statistic_functions):
        method_name = statistic_functions_names[i]
        function = statistic_functions[i](feature1, feature2)
        print("{}({}, {}): {}".format(method_name, features[0], features[1], function))


# def filter_by_feature_hadar(data, feature, value):
#     """
#     :param data:
#     :param feature:
#     :param value:
#     :return:
#     """
#     true_dict = {}
#     false_dict = {}
#     for k, v in data:  # iterate over our data
#         true_list = []  # whichever lines match our condtion of 'value', well add to this list
#         false_list = []  # the rest go here
#         for a, wanted in zip(v, data[feature].values()): # iterate over the wanted feature list and one of the columns
#             if wanted == value:
#                 true_list.append(a)
#             else:
#                 false_list.append(a)
#         true_dict[k] = true_list
#         false_dict[k] = false_list
#     return true_dict, false_dict
