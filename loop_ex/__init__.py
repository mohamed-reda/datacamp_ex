areas = []
for x, y in enumerate(areas):
    print(f"room {x}: {y}")
# Import numpy as np
import numpy as np

# For loop over np_height
for val2 in np.nditer(np_height):
    print(f'{val2} inches')

# For loop over np_baseball
for val in np.nditer(np_baseball):
    print(val)

import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)
for lab, row in brics.iterrows():
    print(lab)
print(row)
