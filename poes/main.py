#%% Import Python Libraries
#from poes.model.poes import poes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, expon, triang, uniform

#%% Generate random values for swi

# Normal distribution
swi_norm = norm.rvs(loc=0.4, scale=0.05, size=1000)
swi_norm = np.clip(swi_norm, 0, 1)

# Lognormal distribution
swi_lognorm = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)
swi_lognorm = np.clip(swi_lognorm, 0, 1)

# Exponential distribution
swi_expon = expon.rvs(loc=0, scale=0.05, size=1000)
swi_expon = np.clip(swi_expon, 0, 1)

# Triangular distribution
swi_tri = triang.rvs(c=0.3, loc=0, scale=1, size=1000)

# Uniform distribution
swi_uni = uniform.rvs(loc=0, scale=1, size=1000)

print("Valores generados para swi:")
print("Normal:", swi_norm)
print("Lognormal:", swi_lognorm)
print("Exponencial:", swi_expon)
print("Triangular:", swi_tri)
print("Uniforme:", swi_uni)