print ("Game 2 . potion mixing chaos")
t1 = input("Enter Ingredient 1 Type (Fire/Water/Earth/Air): ").strip().capitalize()
q1 = int(input("Enter Ingredient 1 Quantity (1-5): "))
t2 = input("Enter Ingredient 2 Type (Fire/Water/Earth/Air): ").strip().capitalize()
q2 = int(input("Enter Ingredient 2 Quantity (1-5): "))

valid_types = ("Fire", "Water", "Earth", "Air")

if (t1 not in valid_types) or (t2 not in valid_types):
    print("Invalid alchemy!")
else:
    mix = (t1, t2)
    match mix:
        case ("Fire", "Water") | ("Water", "Fire"):
            print("Steam Cloud" if q1 == q2 else "Sizzling Sludge")
        case ("Fire", "Earth") | ("Earth", "Fire"):
            print("Lava Bomb" if (q1 + q2) > 6 else "Magma Paste")
        case ("Fire", "Air") | ("Air", "Fire"):
            print("Explosion" if (q1 == 5 or q2 == 5) else "Smoke Screen")
        case ("Water", "Earth") | ("Earth", "Water"):
            print("Mud Golem" if (q1 % 2 == 0 and q2 % 2 == 0) else "Clay Ball")
        case ("Water", "Air") | ("Air", "Water"):
            print("Ice Shard" if abs(q1 - q2) == 1 else "Fog Mist")
        case ("Earth", "Air"):
            print("Dust Devil" if q1 > q2 else "Sand Trap")
        case ("Air", "Earth"):
            print("Dust Devil" if q2 > q1 else "Sand Trap")
        case ("Fire", "Fire"):
            print("Inferno" if (q1 + q2) > 6 else "Ember")
        case ("Water", "Water"):
            print("Torrent" if (q1 + q2) > 6 else "Puddle")
        case ("Earth", "Earth"):
            print("Boulder" if (q1 + q2) > 6 else "Pebble")
        case ("Air", "Air"):
            print("Gale" if (q1 + q2) > 6 else "Breeze")
