def get_data_list(file_name):
    data_file = open("GOOG.csv", "r")
    data_list = [ ] #start with an empty list
    for line_str in data_file: #strip end-of-line, split on
                               #commas, and append items to list
        data_list.append(line_str.strip().split(','))
    return data_list

def get_monthly_averages(data_list):




