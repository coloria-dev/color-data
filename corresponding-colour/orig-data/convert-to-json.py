import json
from pathlib import Path


this_dir = Path(__file__).resolve().parent

for filename in this_dir.glob("*.dat"):

    with open(filename) as f:
        line = f.readline()
        split = line.split()
        whitepoint_test = [float(item) for item in split[:3]]
        whitepoint_refe = [float(item) for item in split[3:]]

        line = f.readline()
        num = int(line.strip())

        test = []
        refe = []
        for _ in range(num):
            line = f.readline()
            split = line.split()
            test.append([float(item) for item in split[:3]])
            refe.append([float(item) for item in split[3:]])

    # transpose
    testT = [[item[k] for item in test] for k in range(3)]
    refeT = [[item[k] for item in refe] for k in range(3)]

    data = {
        "whitepoint-test-xyz": whitepoint_test,
        "whitepoint-reference-xyz": whitepoint_refe,
        "test-xyz": testT,
        "reference-xyz": refeT,
    }

    with open(filename.with_suffix(".json"), "w") as f:
        json.dump(data, f, indent=2)
