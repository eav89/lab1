groupmates = [
{
    "name": "Graham",
    "surname": "Chapman",
    "exams": ["Physics", "English", "History"],
    "marks": [4, 3, 5]
},
{
    "name": "John",
    "surname": "Cleese",
    "exams": ["English", "History", "Chemistry"],
    "marks": [4, 4, 4]
},
{
    "name": "Terry",
    "surname": "Gilliam",
    "exams": ["History", "Chemistry", "Maths"],
    "marks": [5, 5, 5]
},
{
    "name": "Eric",
    "surname": "Idle",
    "exams": ["Chemistry", "Maths", "Economics"],
    "marks": [5, 4, 4]
},
{
    "name": "Terry",
    "surname": "Jones",
    "exams": ["Maths", "Economics", "Physics"],
    "marks": [4, 5, 5]
},
{
    "name": "Michael",
    "surname": "Palin",
    "exams": ["Economics", "Physics", "English"],
    "marks": [5, 3, 5]
}
]

def filter_students(students):
    av_score = float(input("Введите средний балл: "))
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum / len(student["marks"])
        if (round(average, 2) > av_score):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))


filter_students(groupmates)