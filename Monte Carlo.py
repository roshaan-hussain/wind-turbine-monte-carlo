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


wind_speeds = speeds(k, lambda_, 8760)

# Cut in = 4
# Rated speed = 13

power_coff = 0.475
rho = 1.225
r = 50
area = np.pi * r**2


def output_power(power_coff, rho, area, speed):
    return 0.5 * power_coff * rho * area * speed**3


power_output = []

# Iterating through every wind velocity, checking if above or below cut off and rated power speed and calculates the corresponding power.
for v in wind_speeds:
    if v < 4:
        power_output.append(0)
    elif v > 13:
        power_output.append(output_power(power_coff, rho, area, 13))
    else:
        power_output.append(output_power(power_coff, rho, area, v))

print(power_output)
