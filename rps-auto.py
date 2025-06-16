import time
import os
import random
import json
import tkinter as tk
from tkinter import messagebox
inmenu = 1

SAVE_FILE = "rps_rng_save.json"

def tkinter_available():
    try:
        root = tk.Tk()
        root.withdraw()
        root.update()
        root.destroy()
        return True
    except:
        return False

stats_data = {"wins": 0, "losses": 0, "matches": 0, "tkinter_mode": False}
stats_data["tkinter_mode"] = stats_data["tkinter_mode"] and tkinter_available()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhomescreen():
    print(" -----------------------")
    print("|        RPS-RNG        |")
    print("|       By @TheOwenJ       |")
    print(" -----------------------")
    print("1. Start Match")
    print("2. Check Stats")
    print("3. Save / Load")
    print("4. Settings")
    print("5. Exit")
    print(" ")

def playmatch():
    if stats_data["tkinter_mode"]:
        start_tkinter_match()
        return

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
    print("Tkinter Mode:", "On" if stats_data["tkinter_mode"] else "Off")
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
    print("1. Toggle Tkinter Mode (currently: {})".format(
        "On" if stats_data["tkinter_mode"] else "Off"))
    print("2. Back")
    choice = input("Choose: ")

    if choice == "1":
        stats_data["tkinter_mode"] = not stats_data["tkinter_mode"]
        print("Tkinter Mode is now",
              "On" if stats_data["tkinter_mode"] else "Off")
        time.sleep(1)
    elif choice != "2":
        print("Invalid option.")
        time.sleep(1)

    clear()
    printhomescreen()
    inmenu = True

def start_tkinter_match():
    def make_choice(player_choice):
        ai_choice = random.choice(['r', 'p', 's'])
        result = get_result(player_choice, ai_choice)

        result_label.config(
            text=f"You: {choice_names[player_choice]} | A.I.: {choice_names[ai_choice]}\n{result}")

    choice_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    window = tk.Tk()
    window.title("RPS-RNG (Tkinter Mode)")
    window.geometry("300x300")
    window.resizable(False, False)

    tk.Label(window, text="Choose:", font=("Arial", 16)).pack(pady=10)
    tk.Button(window, text="Rock", command=lambda: make_choice('r'), width=15).pack(pady=5)
    tk.Button(window, text="Paper", command=lambda: make_choice('p'), width=15).pack(pady=5)
    tk.Button(window, text="Scissors", command=lambda: make_choice('s'), width=15).pack(pady=5)

    result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=280, pady=10)
    result_label.pack()

    def on_close():
        window.destroy()
        clear()
        printhomescreen()
        global inmenu
        inmenu = True

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

printhomescreen()

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
