import numpy as np
from scipy.stats import norm,lognorm,expon,triang,uniform

#Random values norm
bo_norm=norm.rvs(loc=1.5, scale=0.5, size=1000)
bo_norm=np.where(bo_norm<1,1, bo_norm)
bo_norm=np.where(bo_norm>2,2, bo_norm)

# Random values lognorm
bo_log=lognorm.rvs(0.7,loc=1,scale=0.2,size=1000)
bo_log=np.where(bo_log<1,1, bo_log)
bo_log=np.where(bo_log>2,2, bo_log)

# Random values expon
bo_exp=expon.rvs(loc=1,scale=0.2,size=1000)
bo_exp=np.where(bo_exp<1,1, bo_exp)
bo_exp=np.where(bo_exp>2,2, bo_exp)

# Random values triang
bo_tri=triang.rvs(c=0.3,loc=1,scale=2,size=1000)
bo_tri=np.where(bo_tri<1,1, bo_tri)
bo_tri=np.where(bo_tri>2,2, bo_tri)

# Random values Uniform
bo_unif=uniform.rvs(loc=1,scale=2, size=1000)
bo_unif=np.where(bo_unif<1,1, bo_unif)
bo_unif=np.where(bo_unif>2,2, bo_unif)
print(bo_unif)