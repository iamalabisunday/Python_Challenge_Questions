students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]

def grade_for(avg) -> str:
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

def cal_average(scores) -> float:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_student(student) -> tuple:
    avg = cal_average(student["scores"])
    return (student["name"], avg, grade_for(avg))

# Use map at least once to produce a list of (name, average, grade) tuples.
all_results = list(map(process_student, students))

# Replace the map call with a list comprehension. Which version do you find clearer? Write one sentence explaining why.
# all_results = [process_student(student) for student in students]

# Use filter at least once to produce a list of students who passed (grade A–C).
passed_students = list(filter(lambda record: record[2] in ("A", "B", "C"), all_results))

# Track and print the highest and lowest performing students manually.all_results
highest_score = None
highest_score_name = None

lowest_score = None
lowest_score_name = None

for record in all_results:
    name, avg, grade = record

    if highest_score is None or avg > highest_score:
        highest_score = avg
        highest_score_name = name

    if lowest_score is None or avg < lowest_score:
        lowest_score = avg
        lowest_score_name = name

print("Passed Students:", passed_students)
print("Highest:", highest_score_name, highest_score)
print("Lowest:", lowest_score_name, lowest_score)