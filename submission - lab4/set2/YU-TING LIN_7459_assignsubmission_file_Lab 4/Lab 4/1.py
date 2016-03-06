import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

columns = (a != 0).sum(0)
rows    = (a != 0).sum(1)
