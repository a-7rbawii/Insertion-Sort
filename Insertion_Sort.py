def insertionSort(myList):
    for i in range(0, len(myList)):
        nextItem = myList[i]
        pos = i - 1
        while pos >= 0 and myList[pos] > nextItem:
        #Descending order -> myList[pos] < nextItem:
            myList[pos + 1] = myList[pos]
            pos = pos - 1
        myList[pos + 1] = nextItem

myList = [99, 5, -11, 0, 1, 33, 555]

print("Unsorted array --> {}".format(myList))

insertionSort(myList)

print("Sorted array --> {}".format(myList))