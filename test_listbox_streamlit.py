# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import numpy as np

st.title("Test selectbox")

contact_options=["Email","Phone","Text"]

st.header("Selectbox from a list")

contact_selected=st.selectbox("Preferred contact method",options=contact_options)

st.write("Selectbox returns:",contact_selected," of type",type(contact_selected))


