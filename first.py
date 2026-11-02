number = []

num = int(input("Enter how many numbers: "))

for i in range(num):
    value = float(input("Enter your number in list: "))
    number.append(value)

while True:
    print("\nYour list:", number)
    print("Menu List Searching Program")
    print("1. Search a value")
    print("2. Search an index")
    print("3. Count Occurrences")
    print("4. Add New Number")
    print("5. Exit")

    choice = input("1/2/3/4/5: ")

    if choice == "1":
        n = float(input("Enter a number: "))
        found = False

        for r in range(len(number)):
            if number[r] == n:
                print("Found at index", r)  
                found = True
                break

        if not found:
            print("Not found")

    elif choice == "2":
        index = int(input("Enter an index: "))

        if 0 <= index < len(number):
            print("Value at index", index, "is", number[index])
        else:
            print("Invalid index")

    elif choice == "3":
        count = 0
        n = float(input("Enter your number: "))

        for value in number:
            if value == n:
                count += 1

        print("Number appears", count, "times")

    elif choice == "4":
        new_number = float(input("Enter a number: "))
        number.append(new_number)
        print("Updated list:", number)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")