import string
import numpy as np
import streamlit as st

Ref = {v: k for k, v in enumerate(string.ascii_lowercase)}

with open('words_alpha.txt', 'r') as f:
    content = [x.rstrip() for x in f] 

MAT = np.zeros((26, 32))

for w in content:
    for k, l in enumerate(w):
        MAT[Ref[l]][k] += 1

pctbl = 100 * MAT / MAT.sum(axis=1, keepdims=True)
pctbp = 100 * MAT / MAT.sum(axis=0, keepdims=True)

"""
# Letter frequency
"""

LT, PT = st.tabs(["By Letter", "By Position"])

with LT:
    LSL = st.select_slider('select the letter', options=string.ascii_lowercase)
    st.bar_chart(MAT[Ref[LSL]])

with PT:
    PSL = st.slider('select the position', 0, 32)
    st.bar_chart(MAT[:, PSL])

