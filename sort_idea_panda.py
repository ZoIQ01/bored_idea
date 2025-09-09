import pandas as pd

def panda_sorted(activities: list) -> list:
    df = pd.DataFrame(activities)
    print("\nChoose column to sort:")
    for i, col in enumerate(df.columns, start=1):
        print(f"{i}. {col}")
    try:
        choice = int(input("Choose a number: "))
        column = df.columns[choice - 1]
    except (ValueError, IndexError):
        print("Invalid input!")
        return activities

    order = input("Sort by ascending? (yes/no): ").strip().lower()
    ascending = order == "yes"
    df.sort_values(by=column, ascending=ascending, inplace=True, ignore_index=True)
    print(f"\nSorted by '{column}', ascending={ascending}")
    print(df)
    return df.to_dict(orient="records")
