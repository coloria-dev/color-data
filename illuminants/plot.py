import matplotlib.pyplot as plt
import json
import numpy as np


def plot(names):
    for name in names:
        with open(f"{name}.json") as f:
            data = json.load(f)
        lmbda = data["lambda_nm"]
        x = np.arange(lmbda[0], lmbda[1] + 1, lmbda[2])
        plt.plot(x, data["values"], label=name)
    plt.ylim(0)
    plt.legend()


plot(["f1", "f2", "f3", "f4", "f5", "f6"])
plt.title("standard")
plt.show()


plot(["f7", "f8", "f9"])
plt.title("broadband")
plt.show()


plot(["f10", "f11", "f12"])
plt.title("narrowband")
plt.show()
