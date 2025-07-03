import time
import os
import random
import json
import tkinter as tk

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

stats_data = {
    "wins": 0,
    "losses": 0,
    "matches": 0,
    "tkinter_mode": False
}

# Check Tkinter beschikbaarheid bij start
if not tkinter_available():
    stats_data["tkinter_mode"] = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhomescreen():
    print(" -----------------------")
    print("|        RPS-RNG        |")
    print("|       By @TheOwenJ    |")
    print(" -----------------------")
    print("1. Start Match")
    print("2. Check Stats")
    print("3. Save / Load")
    print("4. Settings")
    print("5. Exit")
    print(" ")

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

def playmatch():
    if stats_data["tkinter_mode"]:
        start_tkinter_match()
        return

    clear()
    while True:
        choice = input("Choose r (Rock), p (Paper), s (Scissors): ").lower()
        if choice in ['r', 'p', 's']:
            break
        print("Invalid choice. Try again.")
        time.sleep(1)
        clear()

    clear()
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
        clear()

    aichoice = random.choice(['r', 'p', 's'])

    choices_str = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    print(f"The A.I. chose: {choices_str[aichoice]}")
    print(f"You chose: {choices_str[choice]}")

    result = get_result(choice, aichoice)
    print(result)
    input("Press Enter to return to the menu...")
    clear()
    printhomescreen()

def stats():
    clear()
    print(" -----------------------")
    print(f"Matches: {stats_data['matches']}")
    print(f"Wins: {stats_data['wins']}")
    print(f"Losses: {stats_data['losses']}")
    print("Tkinter Mode:", "On" if stats_data["tkinter_mode"] else "Off")
    print(" -----------------------")
    input("Press Enter to continue...")
    clear()
    printhomescreen()

def save_data():
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(stats_data, f)
        print("Data saved!")
    except Exception as e:
        print(f"Error saving data: {e}")
    time.sleep(1)

def load_data():
    global stats_data
    try:
        with open(SAVE_FILE, "r") as f:
            loaded = json.load(f)
            # Laad alleen bekende keys (veiligheid)
            for k in stats_data.keys():
                if k in loaded:
                    stats_data[k] = loaded[k]
        print("Data loaded!")
    except FileNotFoundError:
        print("No save file found.")
    except Exception as e:
        print(f"Error loading data: {e}")
    time.sleep(1)
    clear()
    printhomescreen()

def save_load_menu():
    clear()
    print("1. Save Game")
    print("2. Load Game")
    print("3. Back")
    choice = input("Choose: ").strip()

    if choice == "1":
        save_data()
    elif choice == "2":
        load_data()
    elif choice == "3":
        clear()
        printhomescreen()
        return
    else:
        print("Invalid option.")
        time.sleep(1)
    clear()
    printhomescreen()

def settings_menu():
    clear()
    print("Settings:")
    print("1. Toggle Tkinter Mode (currently: {})".format(
        "On" if stats_data["tkinter_mode"] else "Off"))
    print("2. Back")
    choice = input("Choose: ").strip()

    if choice == "1":
        if not tkinter_available():
            print("Tkinter is not available on your system.")
        else:
            stats_data["tkinter_mode"] = not stats_data["tkinter_mode"]
            print("Tkinter Mode is now", "On" if stats_data["tkinter_mode"] else "Off")
    elif choice == "2":
        clear()
        printhomescreen()
        return
    else:
        print("Invalid option.")

    time.sleep(1)
    clear()
    printhomescreen()

def start_tkinter_match():
    choice_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    def make_choice(player_choice):
        ai_choice = random.choice(['r', 'p', 's'])
        result = get_result(player_choice, ai_choice)
        result_label.config(
            text=f"You: {choice_names[player_choice]} | A.I.: {choice_names[ai_choice]}\n{result}"
        )

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

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

def main_loop():
    clear()
    printhomescreen()
    while True:
        menuchoice = input("Choice: ").strip()
        if menuchoice not in ["1", "2", "3", "4", "5"]:
            print("That is not a valid option.")
            time.sleep(1)
            clear()
            printhomescreen()
            continue

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
            break

if __name__ == "__main__":
    main_loop()
