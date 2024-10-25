#%% Import Python Libraries
from poes.model.poes import poes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, expon, triang, uniform

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


#%% Generate random values for porosity
# Random values for Porosity using normal distribution
porosity_norm = norm.rvs(loc=0.4, scale=0.05, size=1000)
# Set min lim
porosity_norm = np.where(porosity_norm < 0, 0, porosity_norm)
# Set  max lim
porosity_norm = np.where(porosity_norm > 0.4, 0.4, porosity_norm)

# Random values for porosity using lognormal distribution
porosity_lognorm = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)
porosity_lognorm = np.where(porosity_lognorm < 0, 0, porosity_lognorm)
porosity_lognorm = np.where(porosity_lognorm > 0.4, 0.4, porosity_lognorm)

# Random values for porosity using exponential distribution
porosity_expon = expon.rvs(loc=0, scale=0.05, size=1000)
porosity_expon = np.where(porosity_expon < 0, 0, porosity_expon)
porosity_expon = np.where(porosity_expon > 0.4, 0.4, porosity_expon)

# Random values for porosity using triangular disribution
porosity_tri = triang.rvs(c=0.3, loc=0, scale=0.4, size=1000)

# Random values for porosity using uniform distribution
porosity_uni = uniform.rvs(loc=0, scale=0.4, size=1000)
print(porosity_uni)

#%% Visualize triangular distribution of porosity
plt.hist(porosity_expon, bins=100)
plt.show()


#%% Generate random values for area
area_norm = norm.rvs(loc=0.4, scale=0.05, size=1000)
area_norm = np.where(area_norm < 0, 0, area_norm)
area_norm = np.where(area_norm > 500, 500, area_norm)

# Random values for area using lognormal distribution
area_lognorm = lognorm.rvs(s=0.5, loc=0, scale=0.05, size=1000)
area_lognorm = np.where(area_lognorm < 0, 0, area_lognorm)
area_lognorm = np.where(area_lognorm > 500, 500, area_lognorm)

# Random values for area using exponential distribution
area_expon = expon.rvs(loc=0, scale=0.05, size=1000)
area_expon = np.where(area_expon < 0, 0, area_expon)
area_expon = np.where(area_expon > 500, 500, area_expon)

# Random values for area using triangular distribution
# area_tri = triang.rvs(c=320, loc=100, scale=300, size=1000)

# Random values for area using uniform distribution
area_uni = uniform.rvs(loc=0, scale=500, size=1000)
print(area_uni)