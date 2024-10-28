def difficulty_level():
    print("Welcome to Hangman!")
    while True:
        # display the menu options
        print("\nChoose Difficulty level (1. Easy / 2. Medium / 3. Hard)")
        level = input("Enter you choise: ").strip()
        if level == "1":
            return ["Kiwi", "Apple", "Banana", "Dog", "Cat", "City"]  # easy words
        elif level == "2":
            return ["Monkey", "library", "Shopping", "School", "Laptop"] #medium
        elif level == "3":
            return ["Pineapple", "Butterfly", "Rainbow","Adventure", "Watermelon", "Strawberry"]  # hard
        else:
            print("Invalid option. Please select 1 for Easy, 2 for Medium, and 3 for Hard.")