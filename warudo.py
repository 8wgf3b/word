import string
import numpy as np


Ref = {v: k for k, v in enumerate(string.ascii_lowercase)}

with open('words_alpha.txt', 'r') as f:
    content = [x.rstrip() for x in f] 

MAT = np.zeros((26, 32))

for w in content:
    for k, l in enumerate(w):
        MAT[Ref[l]][k] += 1

pctbl = 100 * MAT / MAT.sum(axis=1, keepdims=True)
pctbp = 100 * MAT / MAT.sum(axis=0, keepdims=True)

