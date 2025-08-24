import pandas as pd
import os
import csv

FILENAME = "data/activities.csv"
FIELDNAMES = ["id", "activity", "type", "participants", "price", "accessibility", "link"]

def load_activities():
    FILENAME = "data/activities.csv"
    os.makedirs("data", exist_ok=True)
    activities = []
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("Data haven`t been found. File will be created after save.")
        return activities
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["participants"] = int(row["participants"])
            try:
                row["price"] = float(row["price"])
            except:
                row["price"] = row["price"]
            try:
                row["accessibility"] = float(row["accessibility"])
            except:
                row["accessibility"] = row["accessibility"]
            activities.append(row)
    return activities

def add_activities(new_activities, current_activities):
    df_current = pd.DataFrame(current_activities)
    df_new = pd.DataFrame(new_activities)
    combined = pd.concat([df_current, df_new]).drop_duplicates(subset="id", ignore_index=True)
    combined.to_csv(FILENAME, index=False)
    print(f"Total activities: {len(combined)}")
    return combined.to_dict(orient="records")