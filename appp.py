import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.title("champions league Winner Probability")

df = pd.read_csv("champions_league_matches.csv")

teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()

team = st.selectbox("Jamoani tanlang", teams)

# Jamoa oyinlari
matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)]

total_matches = len(matches)

# Yutgan oyinlar hisoblash
wins = 0

for _, row in matches.iterrows():
    if row['HomeTeam'] == team and row['FTHG'] > row['FTAG']:
        wins += 1
    elif row['AwayTeam'] == team and row['FTAG'] > row['FTHG']:
        wins += 1

if total_matches > 0:
    win_rate = wins / total_matches
else:
    win_rate = 0

st.write(f"Umumiy o'yinlar: {total_matches}")
st.write(f"Yutgan o'yinlar: {wins}")
st.write(f"Taxminiy kubok ehtimoli: {round(win_rate*100,2)} %")