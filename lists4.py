import random
myList = ['anna','ben','charlie','dennis','edward','francis']
for i in range(len(myList)):
    name = myList[i]
    #print(name[len(name) - 1])
    #print(name[0])
    #print(len(name))
    print(name[random.randint(0,len(name)-1)])
https://docs.python.org/2/tutorial/datastructures.html
