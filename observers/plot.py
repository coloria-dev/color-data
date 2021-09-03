import json
import matplotlib.pyplot as plt
import numpy as np

filenames = [
    "cie-1931-2.json",
    "cie-1964-10.json",
    "cie-2012-2.json",
    "cie-2012-10.json",
]

for filename in filenames:
    with open(filename) as f:
        data = json.load(f)

    start, stop, step = data["lambda_nm"]
    lmbda = np.arange(start, stop+1, step)
    plt.title(data["name"])
    plt.plot(lmbda, data["xyz"][0], color="r", label="x")
    plt.plot(lmbda, data["xyz"][1], color="g", label="y")
    plt.plot(lmbda, data["xyz"][2], color="b", label="z")
    plt.xlabel("wavelength [nm]")
    plt.show()
