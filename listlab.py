myList = range(10,21) #1
print(myList)

myList = [0,0,0,0,0] #2
print(len(myList))

myList = [] #3
print(myList)

myList = [] #4
for i in range(5):
    myList.append(0)
print(myList)    
    
myList = ["a",5,"doodle",3,10] #5
print(len(myList))

myList = ["a",5,"doodle",3,10] #6
del myList[2]
print(myList)

myList = ["a",5,"doodle",3,10] #7
myList.append("Nana")
print(myList)
print(len(myList))

double = 8.4
myList = ["a",5,"doodle",3,10] #8
del myList[0]
myList.insert(0,double)
print(myList)

