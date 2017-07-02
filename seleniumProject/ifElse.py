# if else statement

i=11
if i % 2 == 0:
    print(str(i) + " is divisible by 2")
else:
    print(str(i) + "is not divisible by 2 ")


# nested is else Statement
today =input("Enter the date")
if today == "Monday":
    print("Monday")
elif today == "Tuesday":
    print("Tesday")
elif today == "Wednessday":
    print("wednessday")
else:
    print("print not found in the list ")

# nested Loop
today = 'holiday'
bankbalance = 2500
if today == "holiday":
    if bankbalance > 2500:
        print("Go shopping")
    else:
        print("stay home")
    
else:
    print('go to office')