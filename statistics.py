import math


def calc_mean(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)


def calc_stdv(values):
    sum = 0
    mean = calc_mean(values)
    for value in values:
        sum += (value - mean) ** 2
    return math.sqrt(sum / (len(values) - 1))


def calc_covariance(values1, values2):
    sum = 0
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)
    for value1, value2 in zip(values1, values2):
        sum += (value1 - mean1) * (value2 - mean2)
    return sum / (len(values1) - 1)
