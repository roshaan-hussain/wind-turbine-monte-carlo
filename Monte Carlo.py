import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Using average values for Cambridgeshire
k = 2
lambda_ = 5.5
turbine_price = 45000
activity = 0.97
yearly_maintenence_costs = 500
yearly_output = []


def one_year_output():
    def speeds(k, lambda_, hours):
        """Provides a list of wind speeds for a specified number of hours using a Weibull distribution"""
        wind_speeds = weibull_min.rvs(c=k, scale=lambda_, size=hours)
        return wind_speeds

    wind_speeds = speeds(k, lambda_, 8760)

    power_coff = 0.475
    rho = 1.225
    r = 2.4
    area = np.pi * r**2

    def output_power(power_coff, rho, area, speed):
        return 0.5 * power_coff * rho * area * speed**3

    power_output = []

    for v in wind_speeds:
        if np.random.random() > activity:
            power_output.append(0)
        elif v < 3.5:
            power_output.append(0)
        elif v > 25:
            power_output.append(0)
        elif v > 12:
            power_output.append(output_power(power_coff, rho, area, 12))
        else:
            power_output.append(output_power(power_coff, rho, area, v))

    numpy_power_output = np.array(power_output)
    # Values in kWh
    power_output_kwh = numpy_power_output/1000
    return yearly_output.append(sum(power_output_kwh))


for i in range(1000):
    one_year_output()

plt.hist(yearly_output, bins=30, color="orange", edgecolor="black")
plt.xlabel("Energy / kWh")
plt.ylabel("Frequencies")
plt.title("Yearly Energy Output")
plt.show()
