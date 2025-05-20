import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import sys
from matplotlib import cm



DATA_DIR =  "./Phase1_logs_final"

st.set_page_config(
    page_title="Metrics Viewer",
    page_icon=":bar_chart:",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.subheader("Available Data")
    
