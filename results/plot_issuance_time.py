import matplotlib.pyplot as plt
import json
import statistics

f = open("issuance_time.json")
data = json.load(f)
print("min ", min(data))
print("max ", max(data))
print("mean ", statistics.mean(data))
print("median ", statistics.median(data), "\n")