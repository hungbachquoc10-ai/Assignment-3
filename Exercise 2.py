inches = 0
while inches >= 0:
    inches = float(input("Enter inches to convert (negative value to quit): "))
    if inches >= 0:
        cm = inches * 2.54
        print(f"{inches} inches is equal to {cm:.2f} cm")
    else:
        print("quit")
    


