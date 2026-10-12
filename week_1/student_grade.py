def grade_for(score: float)-> str:
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F" 


students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    name = student[0]
    scores = student[1:]
        
    total = 0
    for score in scores:
        total += score
            
    avg = total/ len(scores)
        
    grade = grade_for(avg)
            
    print(f"{name} - Average: {avg:.2f} - Grade: {grade}")