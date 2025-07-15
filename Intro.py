#int
#bool
#list
#tuple
#float
#str
#dict

#DUCK TYPING
"""
this is a comment
"""
#num:int = 10
#name: str= "Amani Koros"
#avg: float= 98.9
#names: float =["Mary", "John"]

#print (num)
#print (f'Name {name} Average {avg}')
#print (names)

#for i in names:
#    print(i)

#names.append("Ruth")
#print(names)
#names.pop(1)
#print(names)
#names.clear()
#print("After clearing", names)

#x:int = 0

#while x>2:
#    print(name)
#    print(name)
#    print(name)
#    print(name)
#    print(name)
#    break
#print(name)

#def func() -> None:
#    print(90)
#    age = 20
#    print("Average")
#    for  j in "names":
#        print(j)
#        if age>=20:
#           print("Adults")

#func()
std: dict ={"names": "Alice","Age":21}
print(std)

students: list= [
    {"student name":"Alice","Marks":[94,67,89]},
    {"student name":"Bob", "Marks": [94,98,56]},
    {"student name":"Charlie", "Marks": [94,95,78]},
    {"student name":"John", "Marks": [48,58,97]},
]

def average(marks:list[int])-> float:
    return sum(marks)/len(marks)
print(students)






