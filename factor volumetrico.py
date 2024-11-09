import numpy as np
from scipy.stats import norm, lognorm, expon, triang, uniform

# Valores aleatorios de distribución normal
bo_norm = np.clip(norm.rvs(loc=1.5, scale=0.5, size=1000), 1, 2)
print(bo_norm)

# Valores aleatorios de distribución log-normal
bo_lognorm = np.clip(lognorm.rvs(0.7, loc=1, scale=0.2, size=1000), 1, 2)
print(bo_lognorm)

# Valores aleatorios de distribución exponencial
bo_expon = np.clip(expon.rvs(loc=1, scale=0.2, size=1000), 1, 2)
print(bo_expon)

# Valores aleatorios de distribución triangular
bo_triang = np.clip(triang.rvs(c=0.3, loc=1, scale=2, size=1000), 1, 2)
print(bo_triang)

# Valores aleatorios de distribución uniforme
bo_uniform = np.clip(uniform.rvs(loc=1, scale=2, size=1000), 1, 2)
print(bo_uniform)