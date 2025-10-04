def sql_sorted(conn, table_name, column):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name} ORDER BY {column};"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def sql_sorted_int(conn, table_name="bored_table"):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = %s
    """, (table_name,))
    columns = [row[0] for row in cursor.fetchall()]
    cursor.close()

    if not columns:
        print("list is empty!")
        return []

    print("\nchoose column to sort:")
    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    while True:
        try:
            choice = int(input("number of column: "))
            if 1 <= choice <= len(columns):
                selected_column = columns[choice - 1]
                break
            else:
                print("invalid input!")
        except ValueError:
            print("choose a number!")

    order = input("choose (asc/desc, by default asc): ").strip().lower()
    if order not in ("asc", "desc"):
        order = "asc"

    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name} ORDER BY {selected_column} {order};"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    if not rows:
        print("\nno data have been found")
    else:
        print(f"\nresult: {len(rows)}")
        for row in rows:
            print(row)

    return rows
