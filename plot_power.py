import matplotlib.pyplot as plt
import os
import csv
import numpy as np


dataset = os.walk('data')
fig, axis = plt.subplots()

for root, _, files in dataset:
    for file in sorted(files):
        data = os.path.join(root, file)
        diff = file.split('.', 1)[0]
        # if diff != 'sc4':
        #     continue
        r_p_dpu = []
        with open(data, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                r_p_dpu.append([])
                r_p_dpu[-1].append(float(row['rate']))
                r_p_dpu[-1].append(float(row['power']))
        r_p_dpu.sort(key=lambda x: x[0])
        for idx, (rate, power) in enumerate(r_p_dpu):
            if idx != 0:
                if rate != r_p_dpu[idx-1][0]:
                    r_p_dpu[idx].append((power - r_p_dpu[idx-1][1]) / (rate - r_p_dpu[idx-1][0]))
                else:
                    r_p_dpu[idx].append(r_p_dpu[idx-1][2])
        print(diff)
        print('\n'.join(map(str, r_p_dpu)))
        axis.plot([x[0] for x in r_p_dpu[1:]], [x[2] for x in r_p_dpu[1:]], label=diff, marker='o')

# x = np.arange(96, 100, 0.01)

# sc4 di_co=26 >99.0 y = 4.01864864864875x − 341.67320270271273
# axis.plot(x, 2.6 * x - 339.8)
# axis.scatter(100, 100 * 2.6 - 339.8)
axis.legend()
plt.show()
