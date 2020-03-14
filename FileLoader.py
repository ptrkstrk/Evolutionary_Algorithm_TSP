import numpy as np


def load_cities(filename):
    f = open(filename, "r")
    content = f.readlines()
    cities = []
    type = ""
    started = False
    for line in content:
        if started:
            if line.__contains__("EOF"):
                break
            temp = line.split(" ")
            cord_x = float(temp[1])
            cord_y = float(temp[2])
            cities.append([cord_x, cord_y])
        if line.__contains__("NODE_COORD_SECTION"):
            started = True
        if line.__contains__("EDGE_WEIGHT_TYPE"):
            type = line.split(" ")[-1]
    return np.asarray(cities), type
