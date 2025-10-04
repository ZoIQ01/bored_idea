def sql_filter(conn, table_name, column, value):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name} WHERE {column} = %s;"
    cursor.execute(query, (value,))
    rows = cursor.fetchall()
    cursor.close()
    return rows


def sql_filter_int(conn, table_name="bored_table"):
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

    print("\nchoose column to filter:")
    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    while True:
        try:
            choice = int(input("number of column: "))
            if 1 <= choice <= len(columns):
                selected_column = columns[choice - 1]
                break
            else:
                print("wrong input!")
        except ValueError:
            print("choose a number!")

    filter_value = input(f"Enter a value to filter by column '{selected_column}': ")

    rows = sql_filter(conn, table_name, selected_column, filter_value)

    if not rows:
        print("\nno data has been found")
    else:
        print(f"\ndata found: {len(rows)}")
        for row in rows:
            print(row)

    return rows
