'''
import numpy as np
import pandas as pd

pd.options.display.max_columns = None

var_passengers = pd.read_csv('titanic.csv')


print(var_passengers.head())
print(var_passengers.describe())

print(var_passengers.shape) # matrix dimension
print(var_passengers)
print(var_passengers.head())

import numpy as np

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

suma = np.add(matriz1, matriz2)
print(suma)

suma = matriz1 + matriz2
print(suma)
'''

import numpy as np

from random import random

var_row = []

for _ in range(4):

    var_col = []

    for _ in range(4):
        var_col.append(
            int(random() * 100 / 50))

    var_row.append(var_col)

print(f'Matrix 1 = {var_row}')

var_row = np.where(var_row == 1, True, False)
print(var_row)


