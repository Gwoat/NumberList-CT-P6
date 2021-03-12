"""
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INT's from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value at a specific index
"""

def mainProgram():
    myList = []
    try:
        print("Hello, there! Lt's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("""1. Ad to  a list,
2. Return the value at an index position!
3. Random Search
4.Quit Program""")



        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        else:
            break

    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition.


def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))


def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to see?")
    print(myList[random.randrandint(0, len(myList)-1)])

    


if __name__ == "__main__":
    mainProgram()


            
