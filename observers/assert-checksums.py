import json
import numpy as np


with open("cie-1931-2.json") as f:
    data = json.load(f)
ref = [106.865469489595, 106.856917101172, 106.892251278636]
print(np.sum(data["xyz"], axis=1) - ref)


with open("cie-1964-10.json") as f:
    data = json.load(f)
ref = [116.648519508908, 116.661877102312, 116.673980514647]
print(np.sum(data["xyz"], axis=1) - ref)


with open("cie-2012-2.json") as f:
    data = json.load(f)
ref = [113.04231843009401, 113.04231457233739, 113.04231489170002]
print(np.sum(data["xyz"], axis=1) - ref)


with open("cie-2012-10.json") as f:
    data = json.load(f)
ref = [118.518090997436, 118.5180915321789, 118.518095303296]
print(np.sum(data["xyz"], axis=1) - ref)
