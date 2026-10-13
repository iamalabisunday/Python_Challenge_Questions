def grade(avg: float)-> str:
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"
    
def average(scores: list) -> float:
    total_score = 0
    for score in scores:
        total_score += score
    return total_score / len(scores)

def each_student(student: list) -> dict:
    name = student["name"]
    scores = student["scores"]
    student_average = average(scores)
    student_grade = grade(student_average)
    
    return f"{name} -> Average: {student_average} -> Grade: {student_grade}"

students = [{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}]

all_students = list(map(each_student, students))

print(all_students)