import journal


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
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != "x" and cmd:
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if cmd.lower().strip() == "l":
            list_stries(journal_data)
        elif cmd.lower().strip() == "a":
            add_entry(journal_data)
        elif cmd.lower().strip() != "x" and cmd:
            print(f"Sorry, we don't understand '{cmd}'.")

    print("Good bye!")
    journal.save(journal_name, journal_data)


def list_stries(data):
    print("Your journal entries: ")
    entries = reversed(data)

    for index, entry in enumerate(entries):
        print(f"* [{index+1}] {entry}")


def add_entry(data):
    text = input("Type your entry, <Enter> ")
    journal.add_entry(text, data)


if  __name__ == '__main__'
    main()
