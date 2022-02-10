import time
import json
import os

try:
    open("bookwork.json", "x")
    with open("bookwork.json", "w") as db:
        placeholder = json.loads("{\"placeholder\":\"\"}")
        db.write(json.dumps(placeholder))

except FileExistsError:
    pass

# the funny
os.system("color a")
os.system("title Sparx Bookwork DB")


def main_menu():
    os.system("cls")
    print("///////\n"
          "Welcome to the Sparxmaths Bookwork Database created by theSm1th for internal use.\n"
          "To add an answer, press Enter.\n"
          "To search for an answer, type in a bookwork code and press Enter.\n"
          "///////\n")
    user_input = input("Input : ")

    if user_input == "":
        add_entry_menu()
    else:
        bookwork_ans = search_entry(user_input.upper())
        if bookwork_ans is None:
            print(f"///////\n"
                  f"There is no answer in the database attached to bookwork code {user_input.upper()}.\n"
                  f"///////\n")
            time.sleep(5)
            main_menu()
        else:
            print(f"///////\n"
                  f"The stored answer to {user_input.upper()} is {bookwork_ans}.\n"
                  f"///////\n")
            time.sleep(5)
            main_menu()


def add_entry_menu():
    with open("bookwork.json", "r") as db:
        bookwork_dict = json.loads(db.read())

    os.system("cls")
    print("///////\n"
          "To add a bookwork entry, type the bookwork code, followed by a colon, then the answer to that code.\n"
          "Example:\n"
          "B83: 362.765\n"
          "///////\n")

    user_input = input("Input : ")
    part_input = user_input.partition(":")
    bookwork_dict[part_input[0].upper()] = part_input[2]
    with open("bookwork.json", "w") as db:
        db.write(json.dumps(bookwork_dict, indent=4, sort_keys=True))
    print(f"Added {part_input[0].upper()} entry with value {part_input[2]}.")
    time.sleep(5)
    main_menu()


def search_entry(search_term):
    with open("bookwork.json", "r") as db:
        bookwork_dict = json.loads(db.read())

    for i in bookwork_dict.keys():
        if i == search_term:
            return bookwork_dict[i]


main_menu()
