import csv

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

fig, ax = plt.subplots(figsize=(8, 6))
rc("text", usetex=True)
rc("font", size=16)

with open("snippet/data/N4L001K1/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ring4L001K1 = [float(row[0]) for row in reader]
    ring4L001K1_hist, bin_edges = np.histogram(ring4L001K1, range=(0, 15), bins=15 * 4)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2

with open("snippet/data/N4L001K10/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ring4L001K10 = [float(row[0]) for row in reader]
    ring4L001K10_hist, _ = np.histogram(ring4L001K10, range=(0, 15), bins=15 * 4)


with open("snippet/data/N4L001K50/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ring4L001K50 = [float(row[0]) for row in reader]
    ring4L001K50_hist, _ = np.histogram(ring4L001K50, range=(0, 15), bins=15 * 4)

with open("snippet/data/N4L001K100/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ring4L001K100 = [float(row[0]) for row in reader]
    ring4L001K100_hist, _ = np.histogram(ring4L001K100, range=(0, 15), bins=15 * 4)

with open("snippet/data/N4L01K10/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ringN4L01K10 = [float(row[0]) for row in reader]
    ringN4L01K10_hist, _ = np.histogram(ringN4L01K10, range=(0, 15), bins=15 * 4)

with open("snippet/data/N4L01K0/analyzer_result.txt") as f:
    reader = csv.reader(f)
    ring4L01K0 = [float(row[0]) for row in reader]
    ring4L01K0_hist, _ = np.histogram(ring4L01K0, range=(0, 15), bins=15 * 4)

# plt.plot(bin_centers, ring4L001K1_hist, label="4th K:1\% L:0.01\%")
# plt.plot(bin_centers, ring4L001K10_hist, label="4th K:10\% L:0.01\%")
# plt.plot(bin_centers, ring4L001K50_hist, label="4th K:50\% L:0.01\%")
# plt.plot(bin_centers, ring4L001K100_hist, label="4th K:100\% L:0.01\%")
plt.plot(bin_centers, ringN4L01K10_hist, label="4th K:10\% L:0.1\%")
plt.plot(bin_centers, ring4L01K0_hist, label="4th K:0\% L:0.1\%")
plt.ylabel("frequency", size=20)
plt.xlabel("evaluation function value", size=20)
plt.legend(loc="best")
plt.show()