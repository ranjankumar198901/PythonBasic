
l= [1,2,9,4,5]
L2=["this is a string",77]

list1 =  list()  # create an empty list 
list2 = list([22,33,44])
list3 = list(["tom","jerry","spyke"])
list4 = list("python")

print(l[1])
print(L2[0])
    # x in list 
print(2 in l)
    #x not in list
print(10 not in l)
    #Concatenates 2 string
print("Ranjan" +" " + "Kumar")
    # a * n(n is number of times)
print("a" * 5)
print(5 * "b")
    # find ith element
print(l[3])

    # length
print(len(l))
    #Max
print(max(l))
    #Min
print(min(l))
    #sum
print(sum(l))
    #for Loop

list = [0,1,4,8,3,9,76,876,456]
print(list[0:5])   # this will give list of values from 0 to n-1(5-1)
    # is start is greater than end then it will return empty row 
print(list[9:0])

    # + operator in List
list1=[11,13]
list2=[1,9]
list3= list1 +list2
print(list3)
    #* operator in List
list4 =[1,3,5,7,9]
list5 = list4 *3
print(list5)

    # in and not in list  
l5 =[11,22,33,44,55,16,77]
print(22 in l5)
print(22 not in l5)
print(28 not in l5)

    #traversing in list using loop
l6 =[3,4,5,1,2,7,9,0,11,23,32,43,54,45,46,47]
for i in l6:
    print(i,end="")
   
    #Commonly used List method 
    #Append
L7=[2,4,5,4]
L7.append(9)
print(L7)
    # count number of entry present
print(L7.count(4))
    #Extend
L8=[11,22]
L7.extend(L8)
print(L7)
 
print(L7.index(4))
    #insert insert element in the given index
L7.insert(1,44)
print(L7)

    #Remove remove occurrence of element x from the AddressList
l8=[2,7,3,4,5,6,1,8,6]
l8.remove(6)
print(l8)
    #Reverse 
l8.reverse()
print(l8)

    #sort
l8.sort()
print(l8)

l8.pop()
print(l8)

l8.pop(1)
print(l8)

l9=[x for x in range(10)]
print(l9)

l10 = [x+1 for x in range(10)]
print(l10)

l11 = [x for x in range(10) if x % 2 == 0]
print(l11)

print("Hi")
l12 = [x * 2 for x in range(10) if x % 2 ==0]
print(l12)

