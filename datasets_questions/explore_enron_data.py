#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Person count " + str(len(enron_data))
a_person_features = enron_data.itervalues().next()
print "Person features count " + str(len(a_person_features))
print "POI count " + str(len(filter(lambda features: features['poi'] is True, enron_data.itervalues())))

poi_names_fh = open("../final_project/poi_names.txt", "r")
poi_names_raw_lines = poi_names_fh.readlines()
print "File raw lines " + str(poi_names_raw_lines)
poi_names_lines = poi_names_raw_lines[2:]
print "File lines " + str(len(poi_names_lines))
print "File POI count " + str(len(filter(lambda line: "(y)" in line, poi_names_lines)))

print "James Prentice total stocks " + str(enron_data["PRENTICE JAMES"]["total_stock_value"])
print "Wesley Colwell emails to POI " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print "Jeffrey K Skilling stocks exercised " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

extract = {"SKILLING JEFFREY K": enron_data["SKILLING JEFFREY K"]["total_payments"],
        "LAY KENNETH L": enron_data["LAY KENNETH L"]["total_payments"],
        "FASTOW ANDREW S": enron_data["FASTOW ANDREW S"]["total_payments"]}
print "Who took home the most money " + str(max(extract.iterkeys(), key=(lambda key: extract[key])))
print "Who took home the most money " + str(extract[max(extract.iterkeys(), key=(lambda key: extract[key]))])
print enron_data
print "Persons with quantified salary " + str(len(filter(lambda key: "NaN" != enron_data[key]["salary"],
                                                         enron_data.iterkeys())))
print "Persons with known email " + str(len(filter(lambda key: "NaN" != enron_data[key]["email_address"],
                                                         enron_data.iterkeys())))
persons_without_total_payments = len(filter(lambda key: "NaN" == enron_data[key]["total_payments"],
                                                         enron_data.iterkeys()))
print "Persons without total payments " + str(persons_without_total_payments)
print "% in POIs without total payments " + str(float(len(filter(lambda features: features['poi'], enron_data.itervalues()))) /
                                                float(persons_without_total_payments))



