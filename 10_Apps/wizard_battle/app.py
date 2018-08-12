from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------')
    print('      WIZARD GAME       ')
    print('------------------------')
    print()


def game_loop():

    creatures = [
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature()

    ]

    hero = Wizard()


    while True:

        cmd = input('Do you [a]ttack, [r]un away, [l]ook around: ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, exiting game...bye!!')
            break


if __name__ == "__main__":
    main()
