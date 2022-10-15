import string
import numpy as np


L = string.ascii_lowercase
Ref = {v: k for k, v in enumerate(L)}

with open('words_alpha.txt', 'r') as f:
    content = [x.rstrip() for x in f] 

    MAT = np.zeros((26, 32))

    for w in content:
        for k, l in enumerate(w):
            MAT[Ref[l]][k] += 1
