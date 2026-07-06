print ("Game 3. dungeon door puzzle")
door = input("Choose a door (Red, Blue, Green): ").strip().lower()
weapon = input("Choose a weapon (Sword, Bow, Staff): ").strip().lower()

match (door, weapon):
    case ("red", "sword"):
        print("You survive the red door!")
    case ("red", "bow"):
        print("You die to the Goblin!")
    case ("red", "staff"):
        print("You survive the red door!")
        
    case ("blue", "bow"):
        print("You survive the blue door!")
    case ("blue", "staff"):
        print("You survive the blue door!")
    case ("blue", "sword"):
        print("You die to the Harpy!")
        
    case ("green", "staff"):
        print("You survive the green door!")
    case ("green", "sword"):
        print("You survive the green door!")
    case ("green", "bow"):
        print("You die to the Troll!")
        
    case _:
        print("Invalid choice!")
