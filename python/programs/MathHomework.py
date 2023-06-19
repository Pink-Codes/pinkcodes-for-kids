# MathHomework.py
print ("Python does your Math homework")
problem =  input("Enter a math problem or enter q to quit: ")
while (problem != "q"):
    print ("The answer to " ,problem ,"is " , eval(problem) )
    problem =  input("Enter a math problem or enter q to quit: ")