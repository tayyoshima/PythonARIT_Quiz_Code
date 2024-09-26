import random

roomsAssigned = [1]
room_number = 1
groupList = ["Rat", "Bear", "Wolf", "Dolphin"]
count = 0

print("Welcome to CompanyPro's Team-Building Weekend!")
name = input("Please enter your name (Q to quit)? ")

while name.upper() != 'Q' and count < 50:
    #Your Answer
        #Your Answer
    
    print(f"{name}, your room number is {room_number}")
    roomsAssigned.append(room_number)
    
    group = random.choice(groupList)
    print(f"You will meet with the {group} Group this afternoon.")
    print(roomsAssigned)
    count += 1
    name = input("Please enter your name (Q to quit)? ")

print("Thank you for participating in the Team-Building Weekend!")