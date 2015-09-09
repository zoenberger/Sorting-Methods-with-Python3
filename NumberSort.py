import random


def main(unsorted = []):
    if len(unsorted) <2:
        for i in range(15):
            unsorted.append(random.randint(1,75))

    print()
    print()
    print('List to be sorted: ')
    print(unsorted)
    print()

    print("""\
  1. Bubble Sort 
  2. Selection Sort 
  3. Insertion Sort 
  4. All three!
  5. Cusomize List to be Sorted
  6. Quit Program
          """)
    sortChoice = input("Which sort would you like to use? ")

    try:
        if (int(sortChoice) > 6) or (int(sortChoice) < 1):
            print()
            print("OMG Don't be silly!!!")
            main()
    except ValueError:
        print()
        print("That's not even an integer, man!")
        main()


    choice = int(sortChoice)
    if choice == 5: createList(unsorted)
    elif choice == 6: pass
    else:
        print(unsorted)
        print()

        input("Okay, let's go! Any key to continue.")


        if choice == 1:
            print(bubbleSort(unsorted))
            print('{:*^30}'.format('END OF SORT'))
            main([])
        elif choice == 2:
            print(selectionSort(unsorted))
            print('{:*^30}'.format('END OF SORT'))            
            main([])            
        elif choice == 3:
            print(insertionSort(unsorted))
            print('{:*^30}'.format('END OF SORT'))            
            main([])            
        elif choice == 4:
            allSort(unsorted)
            print('{:*^30}'.format('END OF SORT'))            
            main([])



def selectionSort(unsorted):
    count = len(unsorted)
    passNum = 0
    masterSwaps = 0

    while count > 0:
        swaps = 0
        maxIndex = 0
        maxNum = 0
        for num in range(count):
            if unsorted[num] > maxNum:
                maxNum = unsorted[num]
                maxIndex = num
        unsorted[count -1], unsorted[maxIndex] = unsorted[maxIndex], unsorted[count -1]
        passNum += 1
        if maxIndex == count - 1 :
            count -= 1
            continue
        else:
            masterSwaps += 1
            swaps += 1
        print(unsorted)
        count -=1
        if swaps == 0: break
        

    print()
    print(unsorted)   
    return("Sorted after " + str(passNum) + " passes with " + str(masterSwaps) + " swaps performed")


def insertionSort(unsorted):
    passNum = 0
    inserts = 0
    sortedList = []
    sortedList.append(unsorted.pop(0))


    while len(unsorted) > 0:
        passNum += 1
        count = len(sortedList)
        newNum = unsorted.pop(0)
        compare = count-1
        
        if newNum > sortedList[compare]:
            sortedList.append(newNum)
            inserts += 1
        else:
            while (compare >=0):
                if newNum > sortedList[compare]:
                    sortedList.insert(compare+1,newNum)
                    inserts +=1
                    break
                else:
                    if compare == 0:
                        sortedList.insert(0,newNum)
                        inserts += 1
                        break
                    else:
                        compare -= 1
            
        
        print("unsorted ",unsorted)
        print("sorted", sortedList)
        print()


    print(sortedList)

    return("Sorted after " + str(passNum) + " passes with " + str(inserts) + " inserts performed")
        


def bubbleSort(unsorted):

    count = len(unsorted)
    passNum = 0
    left = 0
    right = left + 1
    masterSwaps = 0

    while count > 0:    
        while left < (count-1):
            swaps = 0
            if unsorted[left] > unsorted[right]:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                swaps += 1
                masterSwaps += 1

            passNum += 1
            print(unsorted)
            
            left +=1
            right +=1
        if swaps == 0: break
        count -= 1
        left = 0
        right = left + 1

    print()
    print(unsorted)
    return("Sorted after " + str(passNum) + " passes with " + str(masterSwaps) + " swaps performed")


def allSort(unsorted):
    print('*** START BUBBLE SORT ***')
    print('UNSORTED: ',unsorted)
    print()
    bubbleString = bubbleSort(unsorted[:])
    print('*** START SELECTION SORT ***')
    print('UNSORTED: ',unsorted)
    print()
    selectionString = selectionSort(unsorted[:])
    print('*** START INSERTION SORT ***')
    print('UNSORTED: ',unsorted)
    print()
    insertionString = insertionSort(unsorted[:])
    print()
    print("Bubble Sort: " + bubbleString)
    print("Selection Sort: " + selectionString)
    print("Insertion Sort: " + insertionString)

    print()
    print()


def createList(unsorted):

    unsorted = unsorted
    print()
    print('Current Unsorted List:')
    print(unsorted)

    print("""
  1. Enter Custom Numbers
  2. Already Sorted Range of X 
  3. Descending Range of X 
  4. Random Range of X integers
  5. Keep current list & return to sort menu.
          """)
    sortChoice = input("Which type of list would you like to create? ")


    try:
        if (int(sortChoice) > 5) or (int(sortChoice) < 1):
            print()
            print("OMG Don't be silly!!!")
            main()
    except ValueError:
        print()
        print("That's not even an integer, man!")
        main()


    choice = int(sortChoice)

    if choice == 1:
        unsorted = []
        addNum = input("Enter integer to add to list. Any other entry to exit: ")
        while (True):
            try:
                unsorted.append(int(addNum))
                addNum = input("Next integer: ")
            except ValueError:
                break
        if len(unsorted) < 2:
            print()
            print("Don't waste my time with such small lists.")
            print()
            createList()
        main(unsorted)
    elif choice == 2:
        unsorted = []
        rangeCount = input("How many items in range? ")
        try:
            if int(rangeCount) < 2 :
                print()
                print("Dude, you can sort that yourself. ")
                createList()
        except ValueError:
            print()
            print("Um, check yo number dude.")
            createList()
        for i in range(1,int(rangeCount)+1):
            unsorted.append(i)
        main(unsorted)
    elif choice == 3:
        unsorted = []
        rangeCount = input("How many items in range? ")
        try:
            if int(rangeCount) < 2 :
                print()
                print("Dude, you can sort that yourself. ")
                createList()
        except ValueError:
            print()
            print("Um, check yo number dude.")
            createList()
        for i in range(int(rangeCount),0,-1):
            unsorted.append(i)
        main(unsorted)
    elif choice == 4:
        unsorted = []
        rangeCount = input("How many random numbers? ")
        try:
            if int(rangeCount) < 2 :
                print()
                print("Dude, you can sort that yourself. ")
                createList()
        except ValueError:
            print()
            print("Um, check yo number dude.")
            createList()
        for i in range(int(rangeCount)):
            unsorted.append(random.randint(1,5*int(rangeCount)) )
        main(unsorted)
    else:
        main(unsorted)


main()
