import pandas as pd
from main import load_or_fetch_initial

panda_list = load_or_fetch_initial(n=100)
activities_df = pd.DataFrame(panda_list)

print(activities_df.head())
def panda_sorted():
    global ideas_df
    if ideas_df.empty:
        print("\nList is empty!")
        return

    print("\nChoose column to sort:")
    for i, col in enumerate(ideas_df.columns, start=1):
        print(f"{i}. {col}")
    try:
        choice = int(input("Choose a number: "))
        column = ideas_df.columns[choice - 1]
    except (ValueError, IndexError):
        print("Invalid input!")
        return

    order = input("Sort by ascending? (yes/no): ").strip().lower()
    ascending = True if order == "yes" else False
    ideas_df.sort_values(by=column, ascending=ascending, inplace=True, ignore_index=True)
    print(f"\nSorted by: {column}, ascending={ascending}")
