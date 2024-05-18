print("Welcom to Quiz!")

playing = input("Do You want to play? Y/n  ")

if playing.lower() != "y":
    quit()

print("Let's Play!")
score =  0
# Q1
answer = input("Q1 :What does CPU Stand For? ")

if answer.lower() == "centeral processing unit":
    print("Hurrrah! Correct")
    score +=1
else:
    print("Alas, You Failed!")

# Q2
answer = input("Q2 :What does GPU Stand For? ")

if answer.lower() == "graphic processing unit":
    print("Hurrrah! Correct")
    score +=1
else:
    print("Alas, You Failed!")

# Q3
answer = input("Q3 :What does RAM Stand For? ")

if answer.lower() == "random access memory":
    print("Hurrrah! Correct")
    score +=1
else:
    print("Alas, You Failed!")

# Q4
answer = input("Q4 :What does ROM Stand For? ")

if answer.lower() == "read only memory":
    print("Hurrrah! Correct")
    score +=1
else:
    print("Alas, You Failed!")

print("You Got " + str(score) + " totally!")