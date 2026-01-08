import random

best_score = None  # Stores minimum attempts across games

while True:
    print("\n🎯 Guess the Number Game")
    print("Choose Difficulty Level:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    choice = input("Enter 1 / 2 / 3: ")

    if choice == "1":
        max_number = 50
        max_attempts = 10
    elif choice == "2":
        max_number = 100
        max_attempts = 7
    elif choice == "3":
        max_number = 200
        max_attempts = 5
    else:
        print("❌ Invalid choice. Try again.")
        continue

    number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("⚠ Please enter a valid number.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")

            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏆 New Best Score!")

            break
        elif guess < number:
            print("📉 Too low! Attempts left:", max_attempts - attempts)
        else:
            print("📈 Too high! Attempts left:", max_attempts - attempts)

    if attempts == max_attempts and guess != number:
        print("\n❌ Game Over!")
        print("The number was:", number)

    if best_score is not None:
        print("⭐ Best Score (minimum attempts):", best_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
