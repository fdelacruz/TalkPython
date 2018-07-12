from datetime import date


def print_header():
    print("-----------------------------------")
    print("            BIRTHDAY APP           ")
    print("-----------------------------------")
    print()


def get_bithday_from_user():
    year = int(input("What year were you born [YYYY] "))
    month = int(input("What month were you born [MM] "))
    day = int(input("What day were you born [DD] "))

    birthday = date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = date(target_date.year, original_date.month, original_date.day)

    daysuntilbirthday = this_year - target_date
    return daysuntilbirthday.days


def print_birthday_information(days):
    if days < 0:
        print(f"Your birthday was {-days} days ago.")
    elif days > 0:
        print(f"Your birthday is in {days} days.")
    else:
        print(f"Well, Happy birthday!!")


def main():
    print_header()
    bday = get_bithday_from_user()
    today = date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
