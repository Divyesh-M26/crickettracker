import csv
import os
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

FILE_NAME = "matches.csv"

# ---------------- CREATE FILE ----------------
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Match", "Runs", "Balls", "Wickets"])


# ---------------- ADD MATCH ----------------
def add_match():
    player = input("Player Name: ")
    match = input("Match Number: ")

    try:
        runs = int(input("Runs Scored: "))
        balls = int(input("Balls Faced: "))
        wickets = int(input("Wickets Taken: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, match, runs, balls, wickets])

    print("✅ Match added successfully!")


# ---------------- SHOW STATS ----------------
def show_stats():
    players = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = row["Player"]
            runs = int(row["Runs"])
            balls = int(row["Balls"])
            wickets = int(row["Wickets"])

            if player not in players:
                players[player] = {
                    "runs": 0,
                    "balls": 0,
                    "wickets": 0,
                    "matches": 0
                }

            players[player]["runs"] += runs
            players[player]["balls"] += balls
            players[player]["wickets"] += wickets
            players[player]["matches"] += 1

    if not players:
        print("No data found!")
        return

    print("\n===== PLAYER ANALYTICS DASHBOARD =====")

    top_player = ""
    best_runs = 0

    for player, data in players.items():

        runs = data["runs"]
        balls = data["balls"]
        matches = data["matches"]
        wickets = data["wickets"]

        strike_rate = (runs / balls) * 100 if balls else 0
        average = runs / matches if matches else 0

        print("\n--------------------------")
        print(f"Player: {player}")
        print("Matches:", matches)
        print("Runs:", runs)
        print("Wickets:", wickets)
        print("Batting Average:", round(average, 2))
        print("Strike Rate:", round(strike_rate, 2))

        if runs > best_runs:
            best_runs = runs
            top_player = player

    print("\n🏆 Top Run Scorer:", top_player, "-", best_runs)


# ---------------- SHOW GRAPH ----------------
def show_graph():
    player_name = input("Enter Player Name: ")

    matches = []
    runs = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Player"].lower() == player_name.lower():
                matches.append(int(row["Match"]))
                runs.append(int(row["Runs"]))

    if not matches:
        print("❌ No data found for this player!")
        return

    combined = sorted(zip(matches, runs))
    matches, runs = zip(*combined)

    plt.plot(matches, runs, marker="o")
    plt.title(f"Runs per Match - {player_name}")
    plt.xlabel("Match")
    plt.ylabel("Runs")
    plt.grid()
    plt.show()


def predict_performance():

    import random
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    runs_list = []
    balls_list = []
    wickets_list = []
    strike_list = []
    impact_list = []
    labels = []

    # ---------------- READ CSV ONCE ----------------
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            runs = int(row["Runs"])
            balls = int(row["Balls"])
            wickets = int(row["Wickets"])

            strike_rate = (runs / balls) * 100 if balls > 0 else 0
            impact_score = runs + (wickets * 20)

            runs_list.append(runs)
            balls_list.append(balls)
            wickets_list.append(wickets)
            strike_list.append(strike_rate)
            impact_list.append(impact_score)

    # ---------------- CREATE LABELS ----------------
    for i in range(len(runs_list)):

        score = (
            runs_list[i] * 0.6 +
            wickets_list[i] * 25 +
            strike_list[i] * 0.3 -
            balls_list[i] * 0.2
        )

        if score > 80:
            labels.append(1)
        else:
            labels.append(0)

    # ---------------- CHECK DATA ----------------
    if len(labels) < 5:
        print("❌ Not enough data for ML!")
        return

    # ---------------- FEATURE MATRIX ----------------
    X = list(zip(
        runs_list,
        balls_list,
        wickets_list,
        strike_list,
        impact_list
    ))

    y = labels

    # ---------------- TRAIN MODEL ----------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    print("\n===== ML MODEL RESULTS =====")
    print("Model Accuracy:", round(accuracy * 100, 2), "%")

    # ---------------- SAMPLE PREDICTION ----------------
    sample = [[50, 40, 1, 125, 70]]
    prediction = model.predict(sample)

    if prediction[0] == 1:
        print("Prediction: GOOD PERFORMANCE 🔥")
    else:
        print("Prediction: AVERAGE / LOW PERFORMANCE ⚠")

# ---------------- RESET ----------------
def reset_data():
    confirm = input("Are you sure? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Match", "Runs", "Balls", "Wickets"])
        print("✅ Data reset done!")
    else:
        print("Cancelled.")


# ---------------- MENU ----------------
while True:
    print("\n=== CRICKET TRACKER ===")
    print("1. Add Match")
    print("2. Show Stats")
    print("3. Show Graph")
    print("4. Reset Data")
    print("5. ML Prediction")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_match()

    elif choice == "2":
        show_stats()

    elif choice == "3":
        show_graph()

    elif choice == "4":
        reset_data()

    elif choice == "5":
        predict_performance()

    elif choice == "6":
        break

    else:
        print("Invalid choice!")
