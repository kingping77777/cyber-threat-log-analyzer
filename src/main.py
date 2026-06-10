import numpy as np

file_path = "data/Global_Cybersecurity_Threats_2015-2024.csv"

data = np.genfromtxt(
    file_path,
    delimiter=",",
    dtype=str,
    encoding="utf-8"
)


# most common attacks count 
attack_types, counts= np.unique(data[1:,2], return_counts=True)
print(attack_types,counts)