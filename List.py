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
3. Random Searchs
4. Add a bunch of numbers
5.Quit Program""")



        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        elif choice == "4":
            addABunch
        else:
            break

    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition.


def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many integers would you like to add?")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange))
    print("Your list is now complete")


def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to see?")
    print(myList[int(indexPos)])



def randomSearch():
    pint("RaNdOm sEarCH?")
    print(myList[random.randrandint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("What you lookin for, PARDNER?    ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            pint("Your item is at index position {}".format(x))

    


if __name__ == "__main__":
    mainProgram()


