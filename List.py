"""
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INT's from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value at a specific index

"""

def mainProgram():
    myMilst = []
    print("Hello, there! Lt's work with lists!")
    print("Choose from the following options. Type a number below!")
    choice = input("1. Ad to  a list , 2. Return the value at an index position!   ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()

    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition.


def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))


def indexValues():


if __name__ == "__main__":
    mainProgram()
            