print("=========================")
print(" TREASURE HUNT ADVENTURE ")
print("=========================")
player_name = input("Enter your name, adventurer: ")
player_age = input("Enter your age: ")
player_favorite_animal = input("Enter your favorite animal: ")
print(f"Welcome, {player_name}!")
print("Your adventure is about to begin.")
print("1. Enter the cave")
print("2. Cross the bridge")
print("3. Walk into the jungle")
print()
player_choice = input("Choose a path: ")
if player_choice == "1":
    print()
    print("You enter the cave and find a treasure chest full of riches!")
elif player_choice == "2":
    print()
    print("You cross the bridge and face a flaming dragon!")
elif player_choice == "3":
    print()
    print("You walk into the jungle and an ancient temple.")
else:
    print()
    print("Invalid choice. Please try again.")
if player_choice == "1":
    player_choice2 = input("Do you want to open the treasure chest? (yes/no): ")
    if player_choice2 == "yes":
        print("You open the treasure chest and find gold and jewels! You win!")
    elif player_choice2 == "no":
        print("You leave the treasure chest untouched and exit the cave safely. You win!")
    else:
        print("Invalid choice. Please try again.")
if player_choice == "2":
    player_choice2 = input("Do you want to fight the dragon or run away? (fight/run): ")
    if player_choice2 == "fight":
        print("You bravely fight the dragon, but you are too weak. You die in battle. Game over.")
    elif player_choice2 == "run":
        print("You run away from the dragon, but it pursues you, it almost catches you. It scrapes your back and injures you badly. You barely escape and survive. You win, but you are badly injured.")
    else:
        print("Invalid choice. Please try again.")
if player_choice == "3":
    player_choice2 = input("Do you want to explore the temple or leave? (explore/leave): ")
    if player_choice2 == "explore":
        print("You explore the temple and find an ancient artifact! You run to get it, but the temple collapses and you are trapped inside. You survive in the collapse, but cannnot escape. Game over.")
    elif player_choice2 == "leave":
        print("You leave the temple and return to the jungle safely. You win!")
        print("Or so you thought, a tiger appears and eats you. Game over.")
    else:
        print("Invalid choice. Please try again.")
player_choice3 = input("Did you enjoy the adventure? (yes/no): ")
if player_choice3 == "yes":
    print(f"I'm glad you enjoyed the adventure, {player_name}!")
elif player_choice3 == "no":
    print(f"I'm sorry to hear that, {player_name}. Maybe next time will be better!")
else:
    print("Invalid choice. Please try again.")