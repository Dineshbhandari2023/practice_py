print ("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))
Bill=0
if height >= 120:
    print ("You can ride a Rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        Bill = 5
        print("Children tickets are $5")
    elif age <= 18:
        Bill = 7
        print("Youth tickets are $7")
    else:
        Bill = 12
        print("Adults tickets are $12")
        
    wants_photos = input("Do you want a photo taken? Y or N.")
    if wants_photos == "y":
        Bill += 3
        print (f"Your final bill is ${Bill}")
else:
    print ("Sorry! you have to grow taller before the ride.")