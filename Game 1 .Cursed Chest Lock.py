print ("Game 1: Cursed Chest Lock")
secret = int(input("Enter a secret 3-digit number (000-999): "))
guess = int(input("Enter your guess (000-999): "))


s3 = secret % 10
s2 = (secret // 10) % 10
s1 = secret // 100


g3 = guess % 10
g2 = (guess // 10) % 10
g1 = guess // 100


pos1 = (s1 == g1)
pos2 = (s2 == g2)
pos3 = (s3 == g3)

exact_matches = pos1 + pos2 + pos3

match_count = 0
if g1 == s1 or g1 == s2 or g1 == s3: match_count += 1
if g2 == s1 or g2 == s2 or g2 == s3: match_count += 1
if g3 == s1 or g3 == s2 or g3 == s3: match_count += 1

if guess == secret:
    print("The chest opens! You found treasure!")
elif exact_matches == 1:
    print("One digit locked in place!")
elif exact_matches == 0 and match_count == 1:
    print("One digit is correct but misplaced!")
elif match_count == 2 or exact_matches == 2:
    print("Two digits are correct!")
else:
    print("Nothing matches. The chest trembles...")
