from new_activities import load_activities, add_activities
from check_activities import check_activities
from rdm_idea import random_idea
from sort_idea_panda import panda_sorted
from filter import panda_filter
from api import fetch_activity
import os
from const import PATH
import pandas as pd


def print_menu():
        print("\nMain Menu")
        print("1. Add an idea")
        print("2. Check all ideas")
        print("3. Filter ideas")
        print("4. Sort by")
        print("5. Get random idea")
        print("0. Exit")

def load_or_fetch_initial(n: int = 100):
    activities = []

    os.makedirs("data", exist_ok=True)
    if os.path.exists(PATH):
        activities = load_activities()

    if len(activities) < n:
        print("Checking local data..")
        print("Data not enough or missing. Fetching from API..")

        all_ids = {a["id"] for a in activities}
        new_ideas = []

        attempts = 0
        while len(activities) + len(new_ideas) < n:
            idea = fetch_activity()
            attempts += 1
            if idea and idea["id"] not in all_ids and idea["id"] not in {i["id"] for i in new_ideas}:
                new_ideas.append(idea)
            if attempts > n * 5:
                print("Can't get enough ideas!")
                break

        activities = add_activities(new_ideas, activities)

    print(f"Total activities loaded: {len(activities)}")
    return activities

def add_ideas_from_api(current_activities: list) -> None:
    try:
        n = int(input("How many ideas to fetch from API? "))
        if n <= 0:
            print("Number must be greater than 0.")
            return
    except ValueError:
        print("Invalid number.")
        return

    new_ideas = []
    attempts = 0
    all_ids = {a["id"] for a in current_activities}
    while len(new_ideas) < n:
        idea = fetch_activity()
        attempts += 1
        if idea and idea["id"] not in all_ids and idea["id"] not in {i["id"] for i in new_ideas}:
            new_ideas.append(idea)
        if attempts > n * 5:
            print("Can't get enough unique ideas!")
            break

    added = add_activities(new_ideas, current_activities)
    print(f"{len(new_ideas)} ideas fetched and added.")

def main():
    activities_list = pd.DataFrame(load_or_fetch_initial(n=100))
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_ideas_from_api(activities_list)
        elif choice == "2":
            check_activities(activities_list)
        elif choice == "3":
            activities_list = panda_filter(activities_list)
        elif choice == "4":
            activities_list = panda_sorted(activities_list)
        elif choice == "5":
            random_idea(activities_list)
        elif choice == "0":
            print("Good bye!")
            break
        else:
            print("Wrong input!")

if __name__ == "__main__":
    main()
