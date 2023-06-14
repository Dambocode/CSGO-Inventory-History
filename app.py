from src import browser, readInventory
import os
from tabulate import tabulate
import asyncio

while True:
    os.system('cls')
    cli_input = input("1. Load Inventory\n2. View Unboxes\n3. View Random Drops\n4. View Rankup Drops\n")

    if cli_input == "1":
        os.system('cls')
        user = input("Enter Username:\n" )
        steamid = input("Enter SteamID:\n" )
        asyncio.get_event_loop().run_until_complete(browser.main(user, steamid))
        input("Press Enter to continue...")
        
    elif cli_input == "2":
        os.system('cls')
        current_dir = os.getcwd()
        file_list = os.listdir(current_dir + "/inventory")
        print(file_list)
        user = input("Enter Username from above:\n" )
        events = readInventory.readInventory(user)
        unboxes = []
        for event in events:
            if "Unlocked a container" in event["event"]:
                unboxes.append(event)
        cases = []
        count_of_cases = []
        knives_unboxed = []
        for event in unboxes:
            if event["case"] not in cases:
                cases.append(event["case"])
                count_of_cases.append({"case": event["case"], "count": 0})
        for case in cases:
            for event in unboxes:
                if event["case"] == case:
                    count_of_cases[cases.index(case)]["count"] += 1
        for item in unboxes:
            # print(item)
            if "★" in str(item["item"]):
                # print("Unboxed a knife!")
                item = {"case": item["case"], "item": item["item"]}
                knives_unboxed.append(item)
        print("Total Cases Opened: " + str(len(unboxes)))
        print(tabulate(count_of_cases, headers="keys", tablefmt="github"))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(tabulate(knives_unboxed, headers="keys", tablefmt="github"))
        input("Press Enter to continue...")
        
    elif cli_input == "3":
        os.system('cls')
        current_dir = os.getcwd()
        file_list = os.listdir(current_dir + "/inventory")
        print(file_list)
        user = input("Enter Username from above:\n" )
        events = readInventory.readInventory(user)
        random_drops = []
        for event in events:
            if "Got an item drop" in event["event"]:
                random_drops.append(event)
        print(tabulate(random_drops, headers="keys", tablefmt="github"))
        input("Press Enter to continue...")


    elif cli_input == "4":
        os.system('cls')
        current_dir = os.getcwd()
        file_list = os.listdir(current_dir + "/inventory")
        print(file_list)
        user = input("Enter Username from above:\n" )
        events = readInventory.readInventory(user)
        rankups = []
        for event in events:
            if "Earned a new rank and got a drop" in event["event"]:
                rankups.append(event)
        print(tabulate(rankups, headers="keys", tablefmt="github"))
        input("Press Enter to continue...")