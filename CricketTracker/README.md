import csv

import os

import matplotlib.pyplot as plt



FILE\_NAME = "matches.csv"



\# Create file with correct headers if it doesn't exist

if not os.path.exists(FILE\_NAME):

&#x20;   with open(FILE\_NAME, "w", newline="") as file:

&#x20;       writer = csv.writer(file)

&#x20;       writer.writerow(\["Player", "Match", "Runs", "Balls", "Wickets"])





def add\_match():

&#x20;   player = input("Player Name: ")

&#x20;   match = input("Match Number: ")

&#x20;   runs = int(input("Runs Scored: "))

&#x20;   balls = int(input("Balls Faced: "))

&#x20;   wickets = int(input("Wickets Taken: "))



&#x20;   with open(FILE\_NAME, "a", newline="") as file:

&#x20;       writer = csv.writer(file)

&#x20;       writer.writerow(\[player, match, runs, balls, wickets])



&#x20;   print("✅ Match added successfully!")





def show\_stats():

&#x20;   players = {}



&#x20;   with open(FILE\_NAME, "r") as file:

&#x20;       reader = csv.DictReader(file)



&#x20;       for row in reader:

&#x20;           player = row\["Player"]

&#x20;           runs = int(row\["Runs"])

&#x20;           balls = int(row\["Balls"])

&#x20;           wickets = int(row\["Wickets"])



&#x20;           if player not in players:

&#x20;               players\[player] = {

&#x20;                   "runs": 0,

&#x20;                   "balls": 0,

&#x20;                   "wickets": 0,

&#x20;                   "matches": 0

&#x20;               }



&#x20;           players\[player]\["runs"] += runs

&#x20;           players\[player]\["balls"] += balls

&#x20;           players\[player]\["wickets"] += wickets

&#x20;           players\[player]\["matches"] += 1



&#x20;   if not players:

&#x20;       print("No data found!")

&#x20;       return



&#x20;   print("\\n===== PLAYER STATS =====")



&#x20;   top\_player = ""

&#x20;   best\_runs = 0



&#x20;   for player, data in players.items():

&#x20;       strike\_rate = (data\["runs"] / data\["balls"]) \* 100 if data\["balls"] > 0 else 0



&#x20;       print(f"\\nPlayer: {player}")

&#x20;       print("Matches:", data\["matches"])

&#x20;       print("Runs:", data\["runs"])

&#x20;       print("Wickets:", data\["wickets"])

&#x20;       print("Strike Rate:", round(strike\_rate, 2))



&#x20;       if data\["runs"] > best\_runs:

&#x20;           best\_runs = data\["runs"]

&#x20;           top\_player = player



&#x20;   print("\\n🏆 Top Performer:", top\_player, "-", best\_runs, "runs")





def show\_graph():

&#x20;   matches = \[]

&#x20;   runs = \[]



&#x20;   with open(FILE\_NAME, "r") as file:

&#x20;       reader = csv.DictReader(file)



&#x20;       for row in reader:

&#x20;           matches.append(row\["Match"])

&#x20;           runs.append(int(row\["Runs"]))



&#x20;   if not matches:

&#x20;       print("No data for graph!")

&#x20;       return



&#x20;   plt.plot(matches, runs, marker="o")

&#x20;   plt.title("Runs per Match")

&#x20;   plt.xlabel("Match")

&#x20;   plt.ylabel("Runs")

&#x20;   plt.grid()

&#x20;   plt.show()





def reset\_data():

&#x20;   confirm = input("Are you sure you want to delete all data? (yes/no): ")



&#x20;   if confirm.lower() == "yes":

&#x20;       with open(FILE\_NAME, "w", newline="") as file:

&#x20;           writer = csv.writer(file)

&#x20;           writer.writerow(\["Player", "Match", "Runs", "Balls", "Wickets"])

&#x20;       print("✅ Data reset successful!")

&#x20;   else:

&#x20;       print("Cancelled.")





while True:

&#x20;   print("\\n=== CRICKET PERFORMANCE TRACKER ===")

&#x20;   print("1. Add Match")

&#x20;   print("2. Show Stats")

&#x20;   print("3. Show Graph")

&#x20;   print("4. Reset Data")

&#x20;   print("5. Exit")



&#x20;   choice = input("Choose option: ")



&#x20;   if choice == "1":

&#x20;       add\_match()



&#x20;   elif choice == "2":

&#x20;       show\_stats()



&#x20;   elif choice == "3":

&#x20;       show\_graph()



&#x20;   elif choice == "4":

&#x20;       reset\_data()



&#x20;   elif choice == "5":

&#x20;       print("Goodbye!")

&#x20;       break



&#x20;   else:

&#x20;       print("Invalid choice!")

