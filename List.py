"""
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INT's from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value at a specific index
"""
import random
myList = []
unique_list = []
def mainProgram():
    
    while True:
        print("Hello, there! Lt's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("""1. Add to  a list,
2. Return the value at an index position!
3. Random Searchs
4. Add a bunch of numbers
5. Linear Search
6. Print List
7. Sort List
8. Recursive Binary Search
9. Iterative Binary Search
10.Quit Program""")


        if choice == "1":
            addToList()
            
        elif choice == "2":
            indexValues()
            
        elif choice == "3":
            randomSearch()
            
        elif choice == "4":
            addABunch()
            
        elif choice == "5":
            linearSearch
            
        elif choice == "6":
            printLists()
            
        elif choice == "7":
            sortList(myList)

        elif choice == "8":
            searchItem = input("What number are you looking for?")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))

        
        elif choice == "9":
            searchItem = input("What are you looking for?  ")
            result = iterativeBinarySearch(unique_list, int(searchItem))
            if result != -1:
                print("Your number is at index position {}.".format(result))
            else:
                print("Your number is not here.")

        
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
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")


def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to see?")
    print(myList[int(indexPos)])

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your  new list? Y/N")
    if showMe.lower() == "y":
        print(unique_list)
        
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsorted?")
        if whichOne.lower() == "sorted":
            print(unique_list)
            
    


    


def randomSearch():
    print("RaNdOm sEarCH?")
    print(myList[random.randrandint(0, len(myList)-1)])


def linearSearch():
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("What you lookin for, PARDNER?    ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            pint("Your item is at index position {}".format(x))
            
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("You did dang found it at index position {}".format(mid))

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)

        else:
            return recursiveBinarySearch(unisue_list, mid +1, high, x)

    else:
        print("Your number isn't here!")
        


def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


if __name__ == "__main__":
    mainProgram()

