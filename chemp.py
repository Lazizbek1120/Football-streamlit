import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="UCL Winner Probability", layout="wide")

st.title(" Champions League Kubok Ehtimoli")

# CSV yuklash
df = pd.read_csv(r"C:\Users\HP\Desktop\Lazizbek\chempions\champions_league_matches.csv")

# Barcha jamoalarni olish
teams = pd.concat([df['home_team'], df['away_team']]).unique()

results = []

for team in teams:
    matches = df[(df['home_team'] == team) | (df['away_team'] == team)]
    total_matches = len(matches)
    wins = 0

    for _, row in matches.iterrows():
        if row['home_team'] == team and row['home_shots_on_target'] > row['away_shots_on_target']:
            wins += 1
        elif row['away_team'] == team and row['away_shots_on_target'] > row['home_shots_on_target']:
            wins += 1

    probability = (wins / total_matches * 100) if total_matches > 0 else 0

    results.append({
        "Team": team,
        "Matches": total_matches,
        "Wins": wins,
        "Win Probability (%)": round(probability, 2)
    })

# DataFrame qilish
prob_df = pd.DataFrame(results)

# Reyting
prob_df = prob_df.sort_values(by="Win Probability (%)", ascending=False)

st.subheader(" Jamoalar reytingi")
st.dataframe(prob_df)

# Eng yuqori ehtimol
top_team = prob_df.iloc[0]
st.success(f" Eng yuqori ehtimol: {top_team['Team']} ({top_team['Win Probability (%)']}%)")

# Grafik
st.subheader("Top 10 Jamoa")

top10 = prob_df.head(10)

plt.figure()
plt.bar(top10["Team"], top10["Win Probability (%)"])
plt.xticks(rotation=45)
plt.xlabel("Team")
plt.ylabel("Win Probability (%)")
st.pyplot(plt)