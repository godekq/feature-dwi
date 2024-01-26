from datetime import datetime

book_maximum_borrowing_days = {"A": 14, "B": 3, "C": 7, "D": 7}

def count_days(borrowing_day, return_day):
    date_format = "%d %B %Y"
    borrow_date = datetime.strptime(borrowing_day, date_format)
    return_date = datetime.strptime(return_day, date_format)
    duration = return_date - borrow_date
    return duration.days + 1

def count_penalty(book_maximum_borrowing_days, borrowing_days):
    if borrowing_days >= book_maximum_borrowing_days:
        return (borrowing_days - book_maximum_borrowing_days) * 100
    else:
        return 0

def price_penalty(book_maximum_borrowing_days, borrowing_date, return_date):
    result = 0
    duration = count_days(borrowing_date, return_date)
    for book, max_days in book_maximum_borrowing_days.items():
        print(f"Denda Buku {book} : {count_penalty(max_days, duration)}")
        result += count_penalty(max_days, duration)
    print(f"Total Denda: {result}")

if __name__ == "__main__":
    a_borrow_date = "28 February 2016"
    a_return_date = "7 March 2016"

    b_borrow_date = "29 April 2018"
    b_return_date = "30 May 2018"

    print(f"Case A {a_borrow_date} until {a_return_date}")
    price_penalty(book_maximum_borrowing_days, a_borrow_date, a_return_date)

    print()

    print(f"Case B {b_borrow_date} until {b_return_date}")
    price_penalty(book_maximum_borrowing_days, b_borrow_date, b_return_date)