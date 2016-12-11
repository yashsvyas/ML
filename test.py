def swap(mylist,i):
    temp1 = mylist[i]
    temp2 = mylist[i+1]
    mylist[i] = temp2
    mylist[i+1] = temp1

def one_scan(mylist):
    for i in range (len(mylist)-1):
        if(mylist[i] >= mylist[i+1]):
            swap(mylist,i)

def sortMyL(L):
    i = 0
    while(i<len(L)):
        one_scan(L)
        i+=1
    print("Sorted list")
    print(L)

def main():
    values = input("Enter numbers(divided by spaces): ")
    valueList = [int(n) for n in values.split()]
    print(sortMyL(valueList))

main()
