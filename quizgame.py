print ("Welcome to my Simple Quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input ("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input ("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input ("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input ("What does UPS stands for? ")
if answer.lower() == "uninterruptible power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input ("What language is this? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1


else:
    print("Incorrect!")

print ("You got " + str(score) + " questions correct")
print ("You got " + str((score/5 *100)) + "%.")