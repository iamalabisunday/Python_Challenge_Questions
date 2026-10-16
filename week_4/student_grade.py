def grade_for(average: float) -> str:
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"
    
def average_for(scores: int) -> float:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def each_student(student: list) -> dict:
    name = student["name"]
    scores = student["scores"]
    average = average_for(scores)
    grade = grade_for(average)
    
    return {
        "name": name,
        "average": average,
        "grade": grade
    }

students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]

all_students = list(map(each_student, students))

pass_students = list(filter(lambda record: record["grade"] in ["A", "B", "C"], all_students))


print("All Students:", all_students)
print("Pass Students:", pass_students)
