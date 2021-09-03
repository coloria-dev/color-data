import json
import numpy as np

with open("cie-1931-2.json") as f:
    data = json.load(f)

ref = [
    106.865_469_489_595,
    106.856_917_101_172,
    106.892_251_278_636
]
print(np.sum(data["xyz"], axis=1) - ref)


with open("cie-1964-10.json") as f:
    data = json.load(f)

ref = [
    116.648_519_508_908,
    116.661_877_102_312,
    116.673_980_514_647,
]
print(np.sum(data["xyz"], axis=1) - ref)
