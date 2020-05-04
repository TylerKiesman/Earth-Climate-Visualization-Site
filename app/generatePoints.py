def add_to_dict(key, value, dict):
    if key in dict:
        dict[key] = dict.get(key) + value
    else:
        dict[key] = value

def land_and_ocean_yearly(filepath):
    file = open(filepath, 'r')
    year_to_temps = dict()
    year_to_uncert = dict()

    #Get rid of first line that only is the column names
    file.readline()
    data = file.readlines()
    for line in data:
        split_data = line.split(',')
        year = int(split_data[0].split('-')[0])
        if year >= 1850:
            monthly_temp = float(split_data[split_data.__len__() - 2])
            monthly_uncert = float(split_data[split_data.__len__() - 1])
            add_to_dict(year, monthly_temp, year_to_temps)
            add_to_dict(year, monthly_uncert, year_to_uncert)
    for key in year_to_temps:
        year_to_temps[key] = year_to_temps.get(key) / 12
        year_to_uncert[key] = year_to_uncert.get(key) / 12
    return [year_to_temps, year_to_uncert]