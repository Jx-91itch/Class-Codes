
students: list= [
    {"student name":"Alice","Marks":[94,67,89]},
    {"student name":"Bob", "Marks": [94,98,56]},
    {"student name":"Charlie", "Marks": [94,95,78]},
    {"student name":"John", "Marks": [48,58,97]},
]

students_2: list= [
    {"student name":"Dan","Marks":[46,64,89]},
    {"student name":"Martin", "Marks": [35,80,70]},
    {"student name":"Mary", "Marks": [60,50,87]},
    {"student name":"Paul", "Marks": [48,58,97]},
]

def average(marks:list[int])-> float:
    return sum(marks)/len(marks)

print("Student names, Marks and Averages:")
for student in students:
    name= student["student name"]
    mark= student["Marks"]
    avg= average(mark)
    print(f"Name:{name} Mark:{mark} Average:{avg:.2f}")


