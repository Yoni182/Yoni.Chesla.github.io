largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" :
        break
    try:
        num = int(inp)
    except:
        print('Invalid input')
        continue
    else:
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
print("Maximum is",largest)
print("Minimum is",smallest)