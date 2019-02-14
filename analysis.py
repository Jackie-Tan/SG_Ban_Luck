import time
start_time = time.time()
import check_prob as cp
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

total_list = []
for i in range(1000):
	total_list.append(cp.run(fixed=True))
mean = np.mean(total_list)
median = np.median(total_list)
skew = stats.skew(total_list)
kurtosis = stats.kurtosis(total_list)
kurtosis_test = stats.kurtosistest(total_list)
std = np.std(total_list)
total_time = time.time() - start_time
print(f"The program took {total_time}s to run.")

plt.hist(total_list, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color="Black", label=None, stacked=False, data=None)
plt.xlabel("Probabilities")
plt.ylabel("Occurrences")
plt.title("Ban Ban Analysis")
plt.text(0.01, 100, f"Mean: {mean}\nMedian: {median}\nStd. Dev.: {std}\nSkew: {skew}\nKurtosis: {kurtosis}\n{kurtosis_test}")
plt.grid(True)
plt.show()