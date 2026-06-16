import time
Score = 0
print("\n")
print("\t\t\t\t*******************************************")
print("\t\t\t\tWELCOME TO NASHRA'S SIMPLE PYTHON QUIZ GAME")
print("\t\t\t\t*******************************************\n")
time.sleep(2)

print("🎮 Now I'm Going to Ask you Some Python Related Quiz Questions🕹️.., So Let's see your Score\n")
time.sleep(5)
print("Let's Start!!..✨\n")
time.sleep(2)

print("Q.1: A Varible stores ______ ?")
print("a.Value of Single DataType")
print("b.Value of Different DataTypes\n")
time.sleep(1)
Ans1 = input("Select the Correct Option: ")


if ( Ans1 == "a" ):
    print("Option (a) is Wrong ❌ , Correct one is (b)\n")
else:
    print("Option (b) is Correct ✅")
    Score += 1
    print(f"The Score is: {Score}")
time.sleep(1)
print("**********************************************************\n\n")
time.sleep(2)

print("Q2: There are total ___ Keywords in Python ?")
print("a.37")
print("b.32\n")
time.sleep(1)
Ans2 = input("Select the Correct Option: ")

if ( Ans2 == "b" ):
    print("Option (b) is Wrong ❌ , Correct one is (a)\n")
else:
    print("Option (a) is Correct ✅")
    Score += 1
    print(f"The Score is: {Score}")
time.sleep(1)
print("**********************************************************\n\n")
time.sleep(2)

print("Q3: Numeric DataType Consist of _____ DataTypes ?")
print("a.Set,Tuple,Dictionaries")
print("b.int,float,complex\n")
time.sleep(1)
Ans3 = input("Select the Correct Option: ")

if ( Ans3 == "a" ):
    print("Option (a) is Wrong ❌ , Correct one is (b)\n")
else:
    print("Option (b) is Correct ✅")
    Score += 1
    print(f"The Score is: {Score}")
    time.sleep(1)
print("**********************************************************\n\n")
time.sleep(2)

print("Q4: How many Building Blocks are there in Python Syllabus ?")
print("a.Only 5")
print("b.More than 5\n")
time.sleep(1)
Ans4 = input("Select the Correct Option: ")

if ( Ans4 == "b" ):
    print("Option (b) is Wrong ❌ , Correct one is (a)\n")
else:
    print("Option (a) is Correct ✅")
    Score += 1
    print(f"The Score is: {Score}")
    time.sleep(1)
print("**********************************************************\n\n")
time.sleep(2)

print("Q5: Python is a Case-Sensitive Language ?")
print("a.False")
print("b.True\n")
time.sleep(1)
Ans5 = input("Select the Correct Option: ")

if ( Ans5 == "a" ):
    print("Option (a) is Wrong ❌ , Correct one is (b)\n")
else:
    print("Option (b) is Correct ✅")
    Score += 1
    print(f"The Score is: {Score}\n")
time.sleep(2)
print(f"Your Score is: {Score}/5\n")
time.sleep(2)

if (Score <= 2 ):
    print("Opp's You Loose!..😓\n")
else:
    print("🏆 Congratulations!!..You Win..🤩\n")

print("\t\t\t\t\t\t*******")
print("\t\t\t\t\t\tTHE END")
print("\t\t\t\t\t\t*******")
