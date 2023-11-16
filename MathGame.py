class MathGames: # base class for math game

    # math game information
    def input(self):
        global x # global allows x to be accessed by other functions
        global y # global allows y to be accessed by other functions

        while True: #infinite loop until conditions are met
            x = input("Enter a two-digit number") #takes user input
            try: #tests code
                x = int(x) #only allows for type int inputs
                break #exits loop
            except ValueError: #if a type other than int is inputted, user inputs again
                print("Please enter a number")

        while True:
            x = int(x)
            if (x < 10 or x > 99):  #error checking prevents non two-digit inputs
                print("Error, please enter a two-digit number")
                x = input() #user inputs until conditions are met
            else:
                y = x * x #squares user input and stores value in a new global variable
                print("\nInput squared is ", y)
                break #exits loop

    def calculate(self):
        array1 = str(y) #Stores squared number into an array as index can be split
        array2 = array1[0:2] #Array slicing allows new array store one half of squared number
        array3 = array1[2:5] #Array slicing allows new array store other half of squared number

        print("\nSplitting square ")
        print("Adding ", array2 + " and", array3)

        global result #global allows result to be accessed outside function
        result = int(array2) + int(array3) #converts arrays to type int to add numbers together
        print("Result is ", result)

    def compare(self):
        global count #used to store information for user score
        if (result == x):
            print("\nYou won!")
            count = 1
        else:
            print("\nBetter luck next time")
            count = 0

    def show_win(self):
        print("\nWinning numbers before you were:")
        if ( x == 10):
            print("none!")
        elif (x <= 45):
            print("10")
        elif (x <= 55):
            print("10, 45")
        else:
            print("10, 45, 55")

        print("-------------------------------------------------------------") #design that separates new game from old game

score:int = 0
i:int = 0
while i == i:
    if (i < 3): # loop allows for 3 attempts, functions are called 'i' times
        user = MathGames()
        user.input()
        user.calculate()
        user.compare()
        user.show_win()
        i = i + 1
        score = score + count
    else:
        print("\nYour score is ",str(score)  + " out of 3") #displays score
        break

