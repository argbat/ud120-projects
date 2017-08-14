#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r"))
print max(data_dict, key=lambda x: data_dict[x]['salary'] if isinstance(data_dict[x]['salary'], int) else float("-inf"))
data_dict.pop('TOTAL', 0)
clean_salary_tuples = filter(lambda x: x[1]['salary'] != 'NaN', data_dict.items())
one_million_salaries = filter(lambda x: x[1]['salary'] > 1000000, clean_salary_tuples)
one_million_salaries_sorted_by_bonus = sorted(one_million_salaries, key=lambda x: x[1]['bonus'])
print one_million_salaries_sorted_by_bonus[-2:]
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

