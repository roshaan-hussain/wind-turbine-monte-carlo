import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Using average values for Cambridgeshire

k = 2
lambda_ = 5.5


def speeds(k, lambda_, hours):
    """Provides a list of wind speeds for a specified number of hours using a Weibull distribution"""
    wind_speeds = weibull_min.rvs(c=k, scale=lambda_, size=hours)
    return wind_speeds


wind_speeds = speeds(k, lambda_, 10)
print(wind_speeds)
