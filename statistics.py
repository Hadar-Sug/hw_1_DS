import math

import Data


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
    """
    prints wanted statistic functions on target based on if treatment is above or below threshold
    :param feature_description: title, (ex:Winter Weekday records)
    :param data: post filtering data
    :param treatment: depending on treatments values, we divide the data we received into 2
    :param target: feature were calculating the statistic functions on
    :param threshold: the threshold
    :param is_above: condition based on which we split the data
    :param statistic_functions: list of wanted functions
    """
    data["flag"] = []  # create another item in our data which will be a list of indicators
    for temp in data[treatment]:  # iterate over treatment based on which well create the indicator list
        data["flag"].append(is_above if temp > threshold else not is_above)
        # assigning True to the values that correspond with is_above condition
    wanted, not_wanted = Data.filter_by_feature(data, "flag", True)
    # get two lists, wanted holding the values were assigned true
    print(f"{feature_description}:")
    Data.print_details(wanted, target, statistic_functions)
