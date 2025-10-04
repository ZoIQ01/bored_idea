import os
import psycopg2
from fetch_data import load_or_fetch
from main_menu import main_menu_int
from list_to_sql import sql_list

def main():
    conn = psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"]
    )

    print("connected to database")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bored_table;")
    count = cursor.fetchone()[0]
    cursor.close()

    if count == 0:
        print("list is empty! load data..")
        ideas = load_or_fetch(100)
        sql_list(conn, ideas)
        print("data have been load successfully")

    main_menu_int(conn)


if __name__ == "__main__":
    main()
