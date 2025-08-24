def filter_activities_list(activities, field, value):
    return [a for a in activities if str(a.get(field, "")) == str(value)]

def filter_activities(activities):
    if not activities:
        print("[WARN] No activities available!")
        return []

    print("Choose field to filter by:")
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

    unique_values = sorted({str(a.get(field, "")) for a in activities})
    print(f"Available values for '{field}':")
    for i, val in enumerate(unique_values, 1):
        print(f"{i}. {val}")

    sel = input("Choose value number: ").strip()
    try:
        value = unique_values[int(sel)-1]
    except:
        print("Invalid selection!")
        return activities

    filtered = filter_activities_list(activities, field, value)
    print(f"[INFO] {len(filtered)} activities matched.")
    return filtered
