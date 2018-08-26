import csv
import numpy as np
with open("media",'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter =' ', quotechar = '"')
        data = [data for data in data_iter]
        data_array = np.asarray(data, dtype = str) 

        print ', '.join(data_array)
