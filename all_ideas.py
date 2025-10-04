def get_all_ideas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bored_table")
    rows = cursor.fetchall()
    cursor.close()
    return rows
