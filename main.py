import sys
import Data
import statistics


def main(argv):
    data = Data.load_data(argv[1], argv[2])
    summer, other_seasons = Data.filter_by_feature(data, "season", 1)
    holiday, weekday = Data.filter_by_feature(data, "is_holiday", 1)
    datas = [summer, holiday, data]
    wanted_features = ["hum", "t1", "cnt"]
    sample_names = ["Summer", "Holiday", "All"]
    wanted_functions = [statistics.calc_mean, statistics.calc_stdv]
    wanted_joint_functions = [statistics.calc_covariance]
    print("Question 1:")
    for name, dataset in zip(sample_names, datas):
        print(f"{name}:")
        Data.print_details(dataset, wanted_features, wanted_functions)
        Data.print_joint_details(dataset, ["t1", "cnt"], wanted_joint_functions, ["Cov"])
    print("\nQuestion 2:")
    threshold = 13.0
    winter, not_winter = Data.filter_by_feature(data, "season", 3)
    winter_holiday, winter_weekday = Data.filter_by_feature(winter, "is_holiday", 1)
    print(f"If t1<={threshold}, then:")
    statistics.population_statistics("Winter Holiday records", winter_holiday, "t1", ["cnt"], threshold, False,
                                     wanted_functions)
    statistics.population_statistics("Winter Weekday records", winter_weekday, "t1", ["cnt"], threshold, False,
                                     wanted_functions)
    print(f"If t1>{threshold}, then:")
    statistics.population_statistics("Winter Holiday records", winter_holiday, "t1", ["cnt"], threshold, True,
                                     wanted_functions)
    statistics.population_statistics("Winter Weekday records", winter_weekday, "t1", ["cnt"], threshold, True,
                                     wanted_functions)


if __name__ == '__main__':
    main(sys.argv)
