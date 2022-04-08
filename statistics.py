import math

import data


def calc_mean(values):
    """
    calculates the mean
    :param values: calculating the mean of these values
    :return: mean
    """
    sum = 0
    for value in values:
        sum += value

    return sum / len(values)


def calc_stdv(values):
    """
    calculates the standard deviation
    :param values: calculating the standard deviation of these values
    :return: standard deviation
    """
    sum = 0
    mean = calc_mean(values)
    for value in values:
        sum += (value - mean) ** 2
    return math.sqrt(sum / (len(values) - 1))


def calc_covariance(values1, values2):
    """
    calculates the covariance of 2 values
    :param values1:first list of values to be used in calculating
    :param values2:second list of values to be used in calculating
    :return:covariance
    """
    sum = 0
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)
    for value1, value2 in zip(values1, values2):
        sum += (value1 - mean1) * (value2 - mean2)

    return sum / (len(values1) - 1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    data["flag"] = []
    for temp in data[treatment]:
        if temp > threshold:
            data["flag"].append(is_above)
        else:
            data["flag"].append(not is_above)
    wanted, not_wanted = data.filter_by_feature(data, "flag", is_above)
    print(f"{feature_description}:\n")
    data.print_details(wanted, target, statistic_functions)
