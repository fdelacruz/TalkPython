def main():
    print_header()
    run_event_loop()


def print_header():
    print("-----------------------------------")
    print("          PERSONAL JOURNAL         ")
    print("-----------------------------------")
    print()


def run_event_loop():

    print("What do you want to do with your journal?")
    cmd = None

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if cmd.lower().strip() == "l":
            list_stries()
        elif cmd.lower().strip() == "a":
            add_entry()
        elif cmd.lower().strip() != "x":
            print(f"Sorry, we don't understand '{cmd}'.")

    print("Good bye!")


def list_stries():
    print("Listing..")


def add_entry():
    print("Adding entry..")


main()
