def generate_global_yearly(filepath):
    file = open(filepath, 'r')
    firstline = file.readline()
    data = file.readlines()