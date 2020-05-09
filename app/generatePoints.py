def add_to_dict(key, value, dict):
    if key in dict:
        dict[key] = dict.get(key) + value
    else:
        dict[key] = value

def state_name_to_code(name):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia (State)': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands': 'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    return us_state_abbrev.get(name)

def state_average_two_years(year1, year2, years_after, filepath):
    file = open(filepath, 'r')
    period1_state_to_average = dict()
    period2_state_to_average = dict()

    # Get rid of first line that only is the column names
    file.readline()
    data = file.readlines()
    for line in data:
        split_data = line.split(',')
        year = int(split_data[0].split('-')[0])
        state = split_data[3]
        country = split_data[4]
        if "United States" in country:
            if split_data[1] == '':
                continue
            monthly_temp = float(split_data[1])
            if year in range(year1, year1 + years_after):
                add_to_dict(state_name_to_code(state), monthly_temp, period1_state_to_average)
            if year in range(year2, year2 + years_after):
                add_to_dict(state_name_to_code(state), monthly_temp, period2_state_to_average)
    for key in period2_state_to_average:
        period2_state_to_average[key] = round(period2_state_to_average.get(key) / (12 * years_after), 2)
        period1_state_to_average[key] = round(period1_state_to_average.get(key) / (12 * years_after), 2)
    return [period1_state_to_average, period2_state_to_average]

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