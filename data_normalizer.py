import os
import csv
from djpower_perfect import djpower_pp


original_dataset = os.walk('data')

def power_normalizer(power, diff, is_sc):
    return power / djpower_pp(diff, is_sc)

def rate_normalizer(rate):
    # if rate < 99.5 or rate >= 99.9:
    #     return None
    return rate

if not os.path.exists('data_normalize'):
    os.mkdir('data_normalize')

with open(os.path.join('data_normalize', 'normalized.csv'), 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['rate', 'power'])

    for root, _, files in original_dataset:
        for file in files:
            data = os.path.join(root, file)
            diff = file.split('.', 1)[0]
            is_sc = diff.startswith('sc')
            diff = int(diff[2 if is_sc else 0:])
            with open(data, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    o_rate = float(row['rate'])
                    o_pow = float(row['power'])
                    rate = rate_normalizer(o_rate)
                    power = power_normalizer(o_pow, diff, is_sc)
                    if rate is None or power is None:
                        continue
                    writer.writerow([rate, power])
                    print(f'{o_rate} -> {rate} / {o_pow} -> {power} @ {file}')
