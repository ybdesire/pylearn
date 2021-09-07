# reference: https://towardsdatascience.com/finding-the-best-distribution-that-fits-your-data-using-pythons-fitter-library-319a5a0972e9
from fitter import Fitter, get_common_distributions, get_distributions
import numpy as np

# 1. get normal distribution data
mu, sigma = 0, 0.1 # mean and standard deviation
data = np.random.normal(mu, sigma, 10000)
print(data.shape)# (1000,)

# 2. fit different distribution
f = Fitter(data,
           distributions=['gamma',
                          'lognorm',
                          "beta",
                          "burr",
                          "norm"])
f.fit()
f.summary()
'''
	sumsquare_error	aic	bic	kl_div
beta	1.379677	236.528768	-88848.069376	inf
norm	1.386285	230.764971	-88818.707132	inf
gamma	1.395113	232.585607	-88746.021598	inf
lognorm	1.446931	233.379202	-88381.328468	inf
burr	3.212436	195.888366	-80396.266524	inf
'''

# 3. get best distribution
f.get_best(method = 'sumsquare_error')# 
'''
{'lognorm': {'s': 0.010758554181293602,
  'loc': -9.238782771404683,
  'scale': 9.240620408137492}}
'''

# 4. get parameter as norm
f.fitted_param["norm"]
# (0.002241549960263148, 0.09955038442398668)
# almost the same as part 1 config
