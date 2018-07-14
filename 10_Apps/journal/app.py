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
    journal_data = []

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if cmd.lower().strip() == "l":
            list_stries(journal_data)
        elif cmd.lower().strip() == "a":
            add_entry(journal_data)
        elif cmd.lower().strip() != "x":
            print(f"Sorry, we don't understand '{cmd}'.")

    print("Good bye!")


def list_stries(data):
    print("Your journal entries: ")
    entries = reversed(data)

    for index, entry in enumerate(entries):
        print(f"* [{index+1}] {entry}")


def add_entry(data):
    text = input("Type your entry, <Enter> ")
    data.append(text)


main()
