def get_random_idea(conn, table_name="bored_table"):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT id, activity, type, participants, price, accessibility, link
        FROM {table_name}
        ORDER BY RANDOM()
        LIMIT 1;
    """)
    row = cursor.fetchone()
    cursor.close()

    if not row:
        return None

    idea = {
        "id": row[0],
        "activity": row[1],
        "type": row[2],
        "participants": row[3],
        "price": row[4],
        "accessibility": row[5],
        "link": row[6]
    }

    return idea
