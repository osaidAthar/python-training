# Constructing list
import copy

l=[]
l1 = list()
print(type(l),type(l1))

# Initializing list

l = [1,2,3,4,5]
l1 = list((1,2,3,4,5))
print(l,l1)

#List Slicing
newList = l[0:3] #it will give create new list with first three value
print(newList)



#Copying list
l2 = l1  #Sallow copy
shallowCopy = copy.copy(l1)
print(l2)
print(shallowCopy)
l1[1]=100 #Changes in main list will reflect in copied list
print(l2) #List is changed now
print("Shallow Copy",shallowCopy)

l3 = copy.deepcopy(l1) #Deep copy
l4 =l1[:] #Deep copy using slicing
print(l3)
print(l4)
l1[2]=300 #Changes will not reflect in copied list
print(l3)
print(l4)


#Sorting 
