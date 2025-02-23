import json
import os

if __name__ == "__main__":
    if not os.path.exists("config.json"):
        print(f"config.json not found or empty, creating...")
        config = {
            "cookies": [],
            "last_cookie_index": {
                "grok-2": 0,
                "grok-3": 0,
                "grok-3-thinking": 0,
            },
            "temporary_mode": True,
        }
        print(f"Enter the cookies you got: ")
        config["cookies"].append(input())
    else:
        with open("config.json", "r") as f:
            config = json.load(f)
    again = True
    while True:
        if again:
            num = len(config["cookies"])
            print(f"You have {num} cookies in your config.json file.")
        print("----------")
        print(f"1. Add")
        print(f"2. Delete all")
        print(f"3. Toggle temporary mode")
        print(f"4. Exit")
        choice = input()
        if choice == "1":
            print(f"Enter the cookies you got: ")
            config["cookies"].append(input())
            again = True
        elif choice == "2":
            config["cookies"] = []
            print(f"Deleted all cookies, enter new cookies:")
            config["cookies"].append(input())
            again = True
        elif choice == "3":
            config["temporary_mode"] = not config["temporary_mode"]
            print(
                f"Temporary mode is now {'on' if config['temporary_mode'] else 'off'}"
            )
            again = False
        elif choice == "4":
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            break
