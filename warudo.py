import streamlit as st
from prempt import MAT, Ref, L


"""
# Letter frequency
"""

LT, PT = st.tabs(["By Letter", "By Position"])

with LT:
    LSL = st.select_slider('select the letter', options=L)
    st.bar_chart(MAT[Ref[LSL]])

with PT:
    PSL = st.slider('select the position', 0, 32)
    st.bar_chart(MAT[:, PSL])

