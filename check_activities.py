def check_activities(df):
    if not df:
        print("[WARN] No activities available!")
        return

    page_size = 10
    total_pages = (len(df) + page_size - 1) // page_size
    current_page = 0

    while True:
        start = current_page * page_size
        end = start + page_size
        page_df = df[start:end]

        print(f"\n--- Page {current_page + 1}/{total_pages} ---")
        for idea in page_df:
            price = idea.get('price', 0)
            accessibility = idea.get('accessibility', 0)

            try:
                price = f"{float(price):.2f}"
            except (ValueError, TypeError):
                price = str(price)
            try:
                accessibility = f"{float(accessibility):.2f}"
            except (ValueError, TypeError):
                accessibility = str(accessibility)

            print(f"id: {idea.get('id', '')} | activity: {idea.get('activity', '')} | type: {idea.get('type', '')} | "
                  f"participants: {idea.get('participants', '')} | price: {price} | accessibility: {accessibility} | link: {idea.get('link', '')}")

        print("\n[n] next page, [p] prev page, [q] quit")
        cmd = input("Command: ").strip().lower()

        if cmd == "n" and current_page < total_pages - 1:
            current_page += 1
        elif cmd == "p" and current_page > 0:
            current_page -= 1
        elif cmd == "q":
            break
        else:
            print("Invalid command!")
