import pandas as pd

def panda_filter(activities: list) -> list:
    df = pd.DataFrame(activities)
    print("\nAvailable filters:")
    print("1. Price")
    print("2. Participants")
    print("3. Type")
    print("4. Accessibility")
    print("5. Link")
    print("0. No filter")
    try:
        choice = int(input("Choose a filter: "))
    except ValueError:
        print("Invalid input.")
        return activities

    if choice == 1:
        try:
            min_price = float(input("Minimum price: "))
            max_price = float(input("Maximum price: "))
            filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
        except ValueError:
            print("Invalid input.")
            return activities
    elif choice == 2:
        try:
            min_participants = int(input("Minimum participants: "))
            max_participants = int(input("Maximum participants: "))
            filtered_df = df[(df['participants'] >= min_participants) & (df['participants'] <= max_participants)]
        except ValueError:
            print("Invalid input.")
            return activities

    elif choice == 3:
        activity_type = input("Enter activity type: ").strip().lower()
        filtered_df = df[df['type'].str.contains(activity_type, case=False, na=False)]
    elif choice == 4:
        try:
            max_accessibility = float(input("Maximum accessibility: "))
            filtered_df = df[df['accessibility'] <= max_accessibility]
        except ValueError:
            print("Invalid input.")
            return activities

    elif choice == 5:
        link = input("Enter link: ").strip().lower()
        filtered_df = df[df['link'].str.contains(link, case=False, na=False)]
    elif choice == 0:
        filtered_df = df
    else:
        print("Invalid choice.")
        return activities

    if filtered_df.empty:
        print("No activities match the selected filter.")
    else:
        print("\nFiltered activities:")
        print(filtered_df)

    return filtered_df.to_dict(orient="records")
