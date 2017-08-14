#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    ## get net worth for age-i
    ## get predicted net worth for age-i
    ## calculate residual error
    ## store it in a dict sorted by value
    ## build cleaned_data with the first 90% of the sorted dict.

    residuals = []

    for age_idx, age_value in enumerate(ages):
        net_worth_for_age = net_worths[age_idx]
        predicted_net_worth_for_age = predictions[age_idx]
        error = abs(net_worth_for_age - predicted_net_worth_for_age)
        residuals.append((age_value, net_worth_for_age, error))

    sorted_residuals = sorted(residuals, key=lambda r: r[2])
    ten_percent_of_residuals = int(len(sorted_residuals) * 0.1)
    start_idx = len(sorted_residuals) - ten_percent_of_residuals
    del sorted_residuals[start_idx:len(sorted_residuals)]

    cleaned_data = sorted_residuals

    return cleaned_data

