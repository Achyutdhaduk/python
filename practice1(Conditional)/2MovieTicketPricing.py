ages = input("give me age:")
age = int(ages)
day = "wednesday"

price =12 if age >= 18 else 8


if day=="wednesday":
    price-=2

print("Ticket Price for you is $",price)
