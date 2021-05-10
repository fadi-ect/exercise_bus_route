# Calculating quotients to determine if the coordinates are close
def is_near(row_1, row_2, RATIO_MIN = 0.99, RATIO_MAX = 1.01): 
    ratios = [row_1["longitude_depart"] / row_2["longitude_depart"], row_1["latitude_depart"] / row_2["latitude_depart"],
              row_1["longitude_destination"] / row_2["longitude_destination"], row_1["latitude_destination"] / row_2["latitude_destination"]]
    for i in ratios:
        if RATIO_MIN <= i <= RATIO_MAX : # Interval set at [0.99 ; 1.01]
            pass
        else:
            return False
    return True

# Get the lines we are interested in
def get_row(row, name):
    if is_near(row, name) == True:
        return row

# We get a single row by cluster
def matches(name, dataframe):
    matches = dataframe.apply(lambda row : get_row(row, name), axis=1)   
    return [elem for elem in matches.to_numpy() if elem is not None]