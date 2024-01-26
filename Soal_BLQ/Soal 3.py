from datetime import datetime

def total_time(in_time, out_time):
    formatter = "%d %B %Y | %H:%M:%S"
    start_date = datetime.strptime(in_time, formatter)
    end_date = datetime.strptime(out_time, formatter)

    return (end_date - start_date).total_seconds() / 3600  # Convert seconds to hours

def parking_price(total_time):
    price = 0

    if total_time <= 8:
        price = total_time * 1000
    elif 8 < total_time <= 24:
        price = 8000
    else:
        price = 15000 + (total_time - 24) * 1000
    return price

def parking_price_calculation(in_time, out_time):
    total_hours = total_time(in_time, out_time)
    print(f"Tariff: {parking_price(total_hours)}")

if __name__ == "__main__":
    in_time = input("Enter the check-in time (dd Month yyyy | HH:mm:ss): ")
    out_time = input("Enter the check-out time (dd Month yyyy | HH:mm:ss): ")

    parking_price_calculation(in_time, out_time)