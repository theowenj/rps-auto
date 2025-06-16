import time
import os
import random
import json

inmenu = 1
SAVE_FILE = "rps_rng_save.json"

# Spelgegevens
stats_data = {"wins": 0, "losses": 0, "matches": 0}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhomescreen():
    print(" -----------------------")
    print("|        RPS-RNG        |")
    print("|       By @OwenJ       |")
    print(" -----------------------")
    print("1. Start Match")
    print("2. Check Stats")
    print("3. Save / Load")
    print("4. Settings")
    print("5. Exit")
    print(" ")

def playmatch():
    global inmenu
    clear()
    choice = input("Choose r (Rock), p (Paper), s (Scissors): ").lower()

    if choice not in ['r', 'p', 's']:
        print("Invalid choice. Try again.")
        time.sleep(1.5)
        clear()
        inmenu = True
        return

    clear()
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
        clear()

    aichoice = random.choice(['r', 'p', 's'])

    print("The A.I. chose:", {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}[aichoice])
    print("You chose:", {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}[choice])

    result = get_result(choice, aichoice)
    print(result)
    input("Press Enter to return to the menu...")
    clear()
    printhomescreen()
    inmenu = True

def get_result(player, ai):
    if player == ai:
        return "It's a draw!"
    elif (player == 'r' and ai == 's') or \
         (player == 'p' and ai == 'r') or \
         (player == 's' and ai == 'p'):
        stats_data["wins"] += 1
        stats_data["matches"] += 1
        return "You win!"
    else:
        stats_data["losses"] += 1
        stats_data["matches"] += 1
        return "You lose!"

def stats():
    global inmenu
    clear()
    print(" -----------------------")
    print("Matches:", stats_data["matches"])
    print("Wins:", stats_data["wins"])
    print("Losses:", stats_data["losses"])
    print(" -----------------------")
    input("Press Enter to continue...")
    clear()
    printhomescreen()
    inmenu = True

def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(stats_data, f)
    print("Data saved!")
    time.sleep(1)

def load_data():
    global stats_data
    try:
        with open(SAVE_FILE, "r") as f:
            stats_data = json.load(f)
        print("Data loaded!")
    except FileNotFoundError:
        print("No save file found.")
    time.sleep(1)

def save_load_menu():
    global inmenu
    clear()
    print("1. Save Game")
    print("2. Load Game")
    print("3. Back")
    choice = input("Choose: ")

    if choice == "1":
        save_data()
    elif choice == "2":
        load_data()
    elif choice == "3":
        pass
    else:
        print("Invalid option.")
        time.sleep(1)

    clear()
    printhomescreen()
    inmenu = True

def settings_menu():
    global inmenu
    clear()
    print("Settings:")
    print("1. (No Tkinter Mode anymore)")
    print("2. Back")
    choice = input("Choose: ")

    if choice != "2":
        print("Invalid option.")
        time.sleep(1)

    clear()
    printhomescreen()
    inmenu = True

# Start
printhomescreen()

# Hoofdlus
while True:
    while inmenu:
        menuchoice = input("Choice: ")

        if menuchoice not in ["1", "2", "3", "4", "5"]:
            print("That is not a valid option.")
            time.sleep(1)
            clear()
            printhomescreen()
        else:
            inmenu = False
            if menuchoice == "1":
                playmatch()
            elif menuchoice == "2":
                stats()
            elif menuchoice == "3":
                save_load_menu()
            elif menuchoice == "4":
                settings_menu()
            elif menuchoice == "5":
                print("Bye!")
                exit()
