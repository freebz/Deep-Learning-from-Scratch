import numpy as np

x = np.array( [[1.0, -0.5], [-2.0, 3.0]] )
print(x)
# [[ 1.  -0.5]
#  [-2.   3. ]]
mask = (x <= 0)
print(mask)
# [[False  True]
#  [ True False]]
