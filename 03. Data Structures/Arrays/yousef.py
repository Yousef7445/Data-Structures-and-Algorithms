# list1 = [2,3,5,2,33,21]

# i = 0

# while i < len(list1):
#     print(list1[i])
#     i += 1

# list2 =[x for x in range(0,5)]
# print(list2)
# list2 = [0,1,2,3,4]
# list3 =[0.5 * x for x in list2]
# print(list3)
# list4 = [x for x in list3 if x <1.5]
# print(list4)
# list1 = ["green","red","blue"]
# list2 = ["red","blue","green"]
# print(list1==list2)

# print(list1 != list2)

# print(list1 >= list2)

# print (list1 > list2)

# print( list1 < list2)

# items = "Welcome to the SCME".split()
# print(items)
# items2 = "34#13#78#45".split("#")
# print(items2)
# def reverse(list1):
#    result = []
    
#    for element in list1:
#        result.insert(0, element)
       
#    return result
# list1 = [1,2,3,4,5,6]
# list2 = reverse(list1)
# print (list2)

# list3 = [2,3,5,7]
# list3.reverse()
# print(list3)
# def selectionsort(lst):
#     for i in range(len(lst)):
#         currentmin = min(lst[i:])
#         currentminindex = i + lst[i:].index(currentmin)

#         if currentminindex !=i:
#             lst[currentminindex],lst[i] = lst[i],currentmin
    
#     return lst
# lst = [0,9,1,100,99,85,3]
# lst.sort()

# print((lst))
# import random
# total = 0
# matrix = []
# numOFrows = int(input("Enter the number of rows: ")) 
# numOFcol = int(input("Enter the number of columns: "))  


# for row in range(numOFrows):
#     matrix.append([])  
#     for col in range(numOFcol):
#         matrix[row].append(random.randrange(0, 100))
#         total += matrix[row][col]
          


# print(matrix, "Total is :"+str(total))
# print("Sum for column " + str(col) + "is :"+ str(total))

# t1 = ()
# t2 =(1,3,5)
# print(t2)
# t3 = tuple([2 * x for x in range(1, 5)])
# print(t3)
# t4 = tuple("abac")
# print(t4)
# t5 = t2 + t3 + t4 
# print(t5)


# # for x in range(0,100):
# #     x = "hello"
# #     print(x)
# s1 = set()
# s2 = {1, 3, 5}
# print(s2)
# s3 =  set([2 * x for x in range(1, 10)])
# print(sum(s3))
# s4 = set("abac")
# print(max(s4))
# s5 = s2 and s3 and s4 
# print(min(s5))


# y1 = {1, 2, 4}
# y2 = {1, 4, 5, 2, 6}
# print(y1.issubset(y2))
dictionary = {"john":40,"karem":2992}
dictionary["yousef"] = 50
# del dictionary["john"]
print(dictionary)
print("john" in dictionary)
print("pop" in dictionary)