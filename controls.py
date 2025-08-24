def control(choice, current_page, total_pages):

    choice = choice.strip().lower()

    if choice == "n" and current_page < total_pages:
        return current_page + 1

    elif choice == "p" and current_page > 1:
        return current_page - 1

    elif choice == "q":
        return None

    else:
        print("[WARN] Wrong input!")

        return current_page