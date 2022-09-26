import imp
import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np


st.title('Here We GOOO!!! :smile:')

points = pd.read_csv('points_table.csv')
matches = pd.read_csv("all_match_results.csv")
players =pd.read_csv("all_players_stats.csv")

st.dataframe(points)
st.write(matches)
st.dataframe(players)


st.balloons()

    