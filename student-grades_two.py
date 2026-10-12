students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]

def grade_for(avg: float) -> str:
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
    
def average(scores: int) -> float:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def each_student(student: dict)-> tuple:
    name = student["name"]
    avg = average(student["scores"])
    grade = grade_for(avg)
    return {
        "name" : name,
        "average" : avg,
        "grade": grade
    }
    

all_student = list(map(each_student, students))

print(all_student)

filting = list(filter(lambda x: x["grade"] in ("A", "B", "C"), all_student))

# print(filting)

highest_name = None
highest_score = None

lowest_name = None
lowest_score = None

for student_average in all_student:
    if highest_score is None or student_average["average"] > highest_score:
        highest_name = student_average["name"]
        highest_score = student_average["average"]
        
    if lowest_score is None or student_average["average"] < lowest_score:
        lowest_name = student_average["name"]
        lowest_score = student_average["average"]
        
message = f"Student with the Highest score: {highest_name} - {highest_score} and Student with the lowest score: {lowest_name} - {lowest_score}"

print(message)