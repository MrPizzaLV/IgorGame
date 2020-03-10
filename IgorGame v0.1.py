from random import randint

print(" _____ _____  ____  _____     _____          __  __ ______ ")
print("|_   _/ ____|/ __ \|  __ \   / ____|   /\   |  \/  |  ____|")
print("  | || |  __| |  | | |__) | | |  __   /  \  | \  / | |__   ")
print("  | || | |_ | |  | |  _  /  | | |_ | / /\ \ | |\/| |  __|  ")
print(" _| || |__| | |__| | | \ \  | |__| |/ ____ \| |  | | |____ ")
print("|_____\_____|\____/|_|  \_\  \_____/_/    \_\_|  |_|______|")

score = 0

tehnikumGo = input("You are Igor. Do you go to RVT?: ")
if tehnikumGo == ("yes"):
    score = score + 1
    print("You decide to go to RVT to make people happy.")
else:
    exit("You made people sad. You lose.\nYour score is: ") + str(score)

lessonNum = randint(1, 3)
if lessonNum == 1:
    lateBy = randint(5, 40)
    if lateBy < 20:
        print("You did it. You made it on time\n")
        score = score + 0
        print("Your score is: " + str(score))
    elif lateBy == 20:
        print("You did it. You made it on time\n")
        score = score + 1
        print("Your score is: " + str(score))
    elif lateBy > 20:
        print("You missed the lesson by a few minutes. The people will surely forgive you\n")
        score = score + 2
        print("Your score is: " + str(score))
    elif lateBy == 40:
        print("At least you came.\n")
        score = score + 5
        print("Your score is: " + str(score))


if lessonNum == 2:
    print("You decide to go to the 2nd lesson because you want to let people sleep.\n")
    score = score + 3
    print("Your score is: " + str(score))
if lessonNum == 3:
    print(
        "You stay home a little bit longer because you remembered to feed the student\nyou have in your basement because he didn't send you the 2nd kursa darbs.\n")
    score = score + 4
    print("Your score is: " + str(score))

igorPercent = str((score / 6) * 100)

print("You are " + igorPercent + "% Igor")
