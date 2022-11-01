import string
import numpy as np
import pickle
from collections import Counter


L = string.ascii_lowercase
Ref = {v: k for k, v in enumerate(L)}

with open('words_alpha.txt', 'r') as f:
    content = [x.rstrip() for x in f]
    ctr = {x: Counter(x) for x in content}

    MAT = np.zeros((26, 32))

    for w in content:
        for k, l in enumerate(w):
            MAT[Ref[l]][k] += 1

def matches(x):
    C = Counter(x)
    return [i for i in content if ctr[i] == ctr[i] & C]