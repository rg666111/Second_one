while True:
    number = []
    num = int(input("Enter a number:"))
    for n in range(num):
	    numbers = float(input("Enter your numbers in list:"))
	    number.append(numbers)

    print("Your list:", number)
    print("Menu list searching program")
    print("1. Search a value")
    print("2. Search an index")
    print("3. Count Occurrences")
    print("4. Add New Numbers")
    
    print("5. Exit")

    choice = input("1/2/3/4/5:")

    if choice == "1":
        n = float(input("Enter a number in 1: "))
        found = False
        for r in range(len(number)):
            if number[r] == n:
                print("Found at index", r)
                print("Your list:", number)
                found = True
                break
        if not found:
            print("Not found")

    elif choice == "2":
        index = int(input("Enter an index: "))
        if 0 <= index < len(number):
            print("Value at index", index, "is", number[index])
            print("Your list:", number)
        else:
            print("Invalid index")
    elif choice =="3":
        count = 0
        print("Your list:", number)

        n = float(input("Enter your number 3: "))

        for value in number:
            if value == n:
                count += 1

        print("Number appears", count, "times")   
    elif choice == "4":
    	 new_number = float(input("Enter a number:"))
    	 number.append(new_number)
    	 print("New List:",new_number)
    elif choice == "5":
       print("Program ended.")
    break