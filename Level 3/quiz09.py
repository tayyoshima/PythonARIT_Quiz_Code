import datetime
dailySpecials=("Spaghetti","Macaroni & Cheese" ,"Meatloaf","Fried Chicken")
weekendSpecials=("Lobster" , "Prime Rib" ,"Parmesan-Crusted Cod")
#Your Answer
#Your Answer
print("My Healthy Eats Delivery")
if today == "Friday" or today =="Saturday" or today =="Sunday":
    print("The weekend specials include:")
    for item in weekendSpecials:
        print(item)
else:
    print("The weekday specials include: ")
    for item in dailySpecials:
        print(item)
#Your Answer
print(f"Pricing specials change in {daysLeft} days")