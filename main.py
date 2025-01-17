print("Welcome to the Lova Calculator")
name_1 = input("What is your name?: ")
name_2 = input("What is his/her name?: ")
name = name_1 + name_2

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

true = T + R + U + E
##########

L = name.count("l")
O = name.count("o")
V = name.count("v")
E = name.count("e")

love = L + O + V + E

########
score = int(str(true) + str (love))

if (score <10 ) or (score > 90):
    print(f" Your score is {score}, you go together like coke & mentos")
elif (score <= 40 ) or (score >= 50):
    print(f" Your score is {score}, Your love is comparable to rush hour traffic. Slow and frustrating, but possible to navigate through persistence and sheer force of will.")
else:
    print(f" Your score is {score}, Your love is like that which a parent with a newborn baby feels for sleep – distant and beyond consideration ")