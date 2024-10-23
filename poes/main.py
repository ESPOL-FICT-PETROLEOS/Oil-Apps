#%% Import Python Libraries
from poes.model.poes import poes
import numpy as np
import pandas as pd

#%% Test poes function using single values
area = 200  # acres
h = 20  # ft
poro = 0.30
swi = 0.65
boi = 1.25  # bbl/stb

stoiip = poes(area, h, poro, swi, boi)
print(f"The stoiip of this reservoir is: {stoiip:.2f} bbl")


#%% Test poes function using array of values
area = np.array([200, 180, 185, 170, 169])
h = np.array([20, 18, 25, 30, 27])
poro = np.array([0.30, 0.31, 0.36, 0.25, 0.28])
swi = np.array([0.65, 0.70, 0.80, 0.77, 0.55])
boi = np.array([1.1, 1.3, 1.4, 1.25, 1.27])

stooip_array = np.round(poes(area, h, poro, swi, boi), 2)
print(stooip_array)