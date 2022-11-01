import streamlit as st
from prempt import MAT, Ref, L, matches


"""
# Letter frequency
"""

LT, PT, AP = st.tabs(["By Letter", "By Position", "Sub-words"])

with LT:
    LSL = st.select_slider('select the letter', options=L)
    st.bar_chart(MAT[Ref[LSL]])

with PT:
    PSL = st.slider('select the position', 0, 32)
    st.bar_chart(MAT[:, PSL])

with AP:
    inp = st.text_input("Word","aa")
    ws = matches(inp)
    st.header(f"There are {len(ws)} words")
    st.write("\n".join(f"* {x}" for x in ws))

