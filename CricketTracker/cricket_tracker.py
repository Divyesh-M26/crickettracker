import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "matches.csv"

# Create file with correct headers if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Match", "Runs", "Balls", "Wickets"])


def add_match():
    player = input("Player Name: ")
    match = input("Match Number: ")
    runs = int(input("Runs Scored: "))
    balls = int(input("Balls Faced: "))
    wickets = int(input("Wickets Taken: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, match, runs, balls, wickets])

    print("✅ Match added successfully!")


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

    print("\n===== PLAYER STATS =====")

    top_player = ""
    best_runs = 0

    for player, data in players.items():
        strike_rate = (data["runs"] / data["balls"]) * 100 if data["balls"] > 0 else 0

        print(f"\nPlayer: {player}")
        print("Matches:", data["matches"])
        print("Runs:", data["runs"])
        print("Wickets:", data["wickets"])
        print("Strike Rate:", round(strike_rate, 2))

        if data["runs"] > best_runs:
            best_runs = data["runs"]
            top_player = player

    print("\n🏆 Top Performer:", top_player, "-", best_runs, "runs")


def show_graph():
    matches = []
    runs = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            matches.append(row["Match"])
            runs.append(int(row["Runs"]))

    if not matches:
        print("No data for graph!")
        return

    plt.plot(matches, runs, marker="o")
    plt.title("Runs per Match")
    plt.xlabel("Match")
    plt.ylabel("Runs")
    plt.grid()
    plt.show()


def reset_data():
    confirm = input("Are you sure you want to delete all data? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Match", "Runs", "Balls", "Wickets"])
        print("✅ Data reset successful!")
    else:
        print("Cancelled.")


while True:
    print("\n=== CRICKET PERFORMANCE TRACKER ===")
    print("1. Add Match")
    print("2. Show Stats")
    print("3. Show Graph")
    print("4. Reset Data")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_match()

    elif choice == "2":
        show_stats()

    elif choice == "3":
        show_graph()

    elif choice == "4":
        reset_data()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")