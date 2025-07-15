#from tkinter.font import names

students: list= [
    {"student name":"Alice","Marks":[94,67,89]},
    {"student name":"Bob", "Marks": [94,98,56]},
    {"student name":"Charlie", "Marks": [94,95,78]},
    {"student name":"John", "Marks": [48,58,97]},
]

def average(marks:list[int])-> float:
    return sum(marks)/len(marks)

print("Student names, Marks and Averages:")
for student in students:
    name= student["student name"]
    mark= student["Marks"]
    avg= average(mark)
    print(f"Name:{name} Mark:{mark} Average:{avg:.2f}")


