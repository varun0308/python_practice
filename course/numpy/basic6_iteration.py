import numpy as np

# Array iteration
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
# -------------------- Same as ----------------------

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
