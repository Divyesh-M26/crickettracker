import streamlit as st
import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier

FILE_NAME = "matches.csv"

st.title("🏏 Cricket AI Analytics Dashboard (Pro Version)")
st.markdown("Single Player + Compare Mode + ML Insights")

# ---------------- LOAD DATA ----------------
players = {}
dataset = []

with open(FILE_NAME, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        player = row["Player"]
        match = int(row["Match"])
        runs = int(row["Runs"])
        balls = int(row["Balls"])
        wickets = int(row["Wickets"])

        strike_rate = (runs / balls) * 100 if balls > 0 else 0
        impact = runs + wickets * 20

        dataset.append([runs, balls, wickets, strike_rate, impact])

        if player not in players:
            players[player] = {
                "runs": 0,
                "balls": 0,
                "wickets": 0,
                "matches": 0,
                "runs_list": [],
                "match_list": []
            }

        players[player]["runs"] += runs
        players[player]["balls"] += balls
        players[player]["wickets"] += wickets
        players[player]["matches"] += 1
        players[player]["runs_list"].append(runs)
        players[player]["match_list"].append(match)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Options")

mode = st.sidebar.radio(
    "Select Mode",
    ["Single Player", "Compare Players"]
)

selected_player = st.sidebar.selectbox(
    "Select Player",
    list(players.keys())
)

# ---------------- PLAYER DATA ----------------
p1 = players[selected_player]

if mode == "Compare Players":
    compare_player = st.sidebar.selectbox(
        "Compare With",
        list(players.keys())
    )
    p2 = players[compare_player]

# ---------------- ML MODEL ----------------
X = []
y = []

for row in dataset:
    X.append(row)

    score = row[0] * 0.5 + row[2] * 25 + row[3] * 0.3

    if score > 80:
        y.append(1)
    else:
        y.append(0)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ---------------- PREDICTION FUNCTION ----------------
def predict(player):
    sr = (player["runs"] / player["balls"]) * 100 if player["balls"] > 0 else 0
    impact = player["runs"] + player["wickets"] * 20

    sample = [[player["runs"], player["balls"], player["wickets"], sr, impact]]
    return model.predict(sample)[0]

# ---------------- SINGLE PLAYER VIEW ----------------
st.subheader(f"📊 Player: {selected_player}")

col1, col2, col3 = st.columns(3)

col1.metric("Matches", p1["matches"])
col2.metric("Runs", p1["runs"])
col3.metric("Wickets", p1["wickets"])

avg = p1["runs"] / p1["matches"]
sr = (p1["runs"] / p1["balls"]) * 100 if p1["balls"] > 0 else 0

st.write("Batting Average:", round(avg, 2))
st.write("Strike Rate:", round(sr, 2))

# ---------------- ML RESULT ----------------
st.subheader("🤖 ML Prediction")

result = predict(p1)

if result == 1:
    st.success("🔥 Elite Performance Player")
else:
    st.warning("⚠ Average / Developing Player")

# ---------------- GRAPH ----------------
st.subheader("📈 Performance Trend")

st.line_chart({
    selected_player: p1["runs_list"]
})

# ---------------- COMPARISON (ONLY IF SELECTED) ----------------
if mode == "Compare Players":

    st.subheader("⚔ Player Comparison")

    st.write(selected_player, "vs", compare_player)

    st.write("Runs:", p1["runs"], "vs", p2["runs"])
    st.write("Wickets:", p1["wickets"], "vs", p2["wickets"])

    st.subheader("📊 Comparison Graph")

    st.line_chart({
        selected_player: p1["runs_list"],
        compare_player: p2["runs_list"]
    })
