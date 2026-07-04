import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# ======================
# LOAD DATA (ONCE)
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("startup_funding.csv")

    df.dropna(subset=['Amount in USD'], inplace=True)

  