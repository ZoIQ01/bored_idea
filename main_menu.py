import psycopg2
from all_ideas import get_all_ideas
from filter_sql import sql_filter_int
from pages_int import interactive_all_ideas
from dotenv import load_dotenv
from pathlib import Path
import os
from rdm_sql import get_random_idea
from sort_sql import sql_sorted_int
from new_idea import add_n_ideas
from list_to_sql import sql_list

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

conn = psycopg2.connect(
    dbname=os.environ["DB_NAME"],
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    port=os.environ["DB_PORT"]
)

def print_menu():
    print("\n=== MAIN MENU ===")
    print("1. Add new ideas")
    print("2. Show all ideas")
    print("3. Filter ideas")
    print("4. Sort ideas")
    print("5. Get random idea")
    print("0. Exit")


def main_menu_int(conn):
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                n = int(input("how much ideas would you like to add? "))
                new_ideas = add_n_ideas(n)
                if new_ideas:
                    sql_list(conn, new_ideas)
                    print(f"added {len(new_ideas)} new ideas")
            except ValueError:
                print("enter a number!")

        elif choice == "2":
            ideas = get_all_ideas(conn)
            interactive_all_ideas(ideas)

        elif choice == "3":
            rows = sql_filter_int(conn, table_name="bored_table")
            interactive_all_ideas(rows)

        elif choice == "4":
            rows = sql_sorted_int(conn, table_name="bored_table")
            interactive_all_ideas(rows)

        elif choice == "5":
            idea = get_random_idea(conn, table_name="bored_table")
            if idea:
                print(f"\n🎲 Random idea:")
                print(f"id={idea['id']}, activity={idea['activity']}, type={idea['type']}, "
                      f"participants={idea['participants']}, price={idea['price']}, "
                      f"accessibility={idea['accessibility']}, link={idea['link']}")
            else:
                print("no ideas found in database.")

        elif choice == "0":
            print("good bye!")
            conn.close()
            break

        else:
            print("wrong input!")

