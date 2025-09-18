import pandas as pd


def panda_filter(activities: list, price_range=None, participants_range=None, activity_type=None,
                 max_accessibility=None, link=None) -> list:
    df = pd.DataFrame(activities)

    if price_range:
        min_price, max_price = price_range
        df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

    if participants_range:
        min_p, max_p = participants_range
        df = df[(df['participants'] >= min_p) & (df['participants'] <= max_p)]

    if activity_type:
        df = df[df['type'].str.contains(activity_type, case=False, na=False)]

    if max_accessibility is not None:
        df = df[df['accessibility'] <= max_accessibility]

    if link:
        df = df[df['link'].str.contains(link, case=False, na=False)]

    return df.to_dict(orient="records")

def filter_menu(activities: list):
    while True:
        print("\nAvailable filters:")
        print("1. Price")
        print("2. Participants")
        print("3. Type")
        print("4. Accessibility")
        print("5. Link")
        print("0. No filter")

        choice = input("Choose a filter: ").strip()
        if choice == "1":
            min_price = float(input("Minimum price: "))
            max_price = float(input("Maximum price: "))
            filtered = panda_filter(activities, price_range=(min_price, max_price))
        elif choice == "2":
            min_p = int(input("Minimum participants: "))
            max_p = int(input("Maximum participants: "))
            filtered = panda_filter(activities, participants_range=(min_p, max_p))
        elif choice == "3":
            t = input("Enter activity type: ").strip().lower()
            filtered = panda_filter(activities, activity_type=t)
        elif choice == "4":
            max_a = float(input("Maximum accessibility: "))
            filtered = panda_filter(activities, max_accessibility=max_a)
        elif choice == "5":
            l = input("Enter link: ").strip().lower()
            filtered = panda_filter(activities, link=l)
        elif choice == "0":
            filtered = activities
        else:
            print("Invalid choice.")
            continue

        if not filtered:
            print("No activities match the selected filter.")
        else:
            print(pd.DataFrame(filtered))
        return filtered

