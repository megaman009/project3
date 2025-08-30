from collections import Counter

magazine = input("Enter the magazine text: ")
notebook = input("Enter the ransom note text: ")

mag, note = Counter(magazine), Counter(notebook)

if mag & note == note:
    print("you have enough letters")
else:
    print("you do not have enough letters")

    missing = note - mag
    print(" the missing letters are: ")

    for char, count in missing.items():
        print(f"'{char}' is short by {count}")
