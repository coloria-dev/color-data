import json

import numpy as np
import openpyxl
import yaml

wb = openpyxl.load_workbook("BFD-P.xlsx")

ws = wb.worksheets[0]
dv = [ws[f"A{k}"].value for k in range(3, 2779)]

white = [ws["B3"].value, ws["C3"].value, ws["D3"].value]

pairs = [
    [
        [ws[f"E{k}"].value, ws[f"F{k}"].value, ws[f"G{k}"].value],
        [ws[f"H{k}"].value, ws[f"I{k}"].value, ws[f"J{k}"].value],
    ]
    for k in range(3, 2779)
]

# find duplicates in the pairs
pairs = np.array(pairs)
pairs = pairs.reshape(-1, 3)
uniques, idx = np.unique(pairs, return_inverse=True, axis=0)
idx = idx.reshape((-1, 2))

d = {"reference_white": white, "dv": dv, "pairs": idx.tolist(), "xyz": uniques.tolist()}

with open("bfd-p.yaml", "w") as f:
    yaml.dump(d, f)


with open("bfd-p.json", "w") as f:
    json.dump(d, f)
