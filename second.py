lower = 1
higher = 100
attempt = 0

while lower <= higher:
    guess = (lower + higher) // 2
    attempt += 1

    print(f"Computer's Guess #{attempt}: Is it {guess}?")

    ch = input("'h' = too high, 'l' = too low, 'c' = correct: ").lower()

    if ch == 'c':
        print(f"Awesome! The computer found your number {guess} in {attempt} attempts!")
        break

    elif ch == 'h':
        higher = guess - 1

    elif ch == 'l':
        lower = guess + 1

    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")
        attempt -= 1
        continue

if lower > higher:
    print("\nWait a minute... Your answers contradicted each other!")