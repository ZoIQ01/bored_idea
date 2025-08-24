def sort_activities_list(activities, field, ascending=True):
    def key(a):
        val = a.get(field, "")
        try:
            return float(val)
        except (ValueError, TypeError):
            return str(val).lower()
    return sorted(activities, key=key, reverse=not ascending)

def sort_activities(activities):
    if not activities:
        print("[WARN] No activities available!")
        return activities

    print("Choose field to sort by:")
    print("1. id")
    print("2. activity")
    print("3. type")
    print("4. participants")
    print("5. price")
    print("6. accessibility")
    print("7. link")

    choice = input("Enter number: ").strip()
    field_map = {
        "1": "id",
        "2": "activity",
        "3": "type",
        "4": "participants",
        "5": "price",
        "6": "accessibility",
        "7": "link"
    }
    field = field_map.get(choice)
    if not field:
        print("Invalid choice!")
        return activities

    direction = input("Choose sort direction: 1. Ascending 2. Descending: ").strip()
    ascending = direction != "2"

    sorted_list = sort_activities_list(activities, field, ascending)
    print(f"[INFO] Activities sorted by '{field}' ({'ascending' if ascending else 'descending'}).")
    return sorted_list