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
import random

matrix = []
numOFrows = int(input("Enter the number of rows: "))  # استخدام int بدل eval
numOFcol = int(input("Enter the number of columns: "))  # استخدام int بدل eval

# بناء المصفوفة
for row in range(numOFrows):
    matrix.append([])  # إضافة قائمة فارغة لكل صف
    for col in range(numOFcol):
        matrix[row].append(random.randrange(0, 100))  # إضافة قيمة عشوائية بين 0 و 100

# طباعة المصفوفة
print(matrix)
