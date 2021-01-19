student_name = input('name: ')
student_homework = int(input('homework 25/'))
student_assesment = int(input('assesment 50/'))
student_final_exam = int(input('final exam 100/'))


def grade_calc (homework, assesment, final_exam):
    if homework > 25 or assesment > 50 or final_exam > 100:
        return "invalid scores entered"
    total = homework + assesment + final_exam
    grade = (total / 175) * 100
    return grade


def grade_boundries(percent_score):
    final_grade = ""
    if percent_score > 80:
        final_grade = "A"
    elif percent_score > 70:
        final_grade = "B"
    elif percent_score > 60:
        final_grade = "C"
    elif percent_score > 50:
        final_grade = "D"
    else: 
        final_grade = "F"
    
    return final_grade


grade = grade_calc(student_homework, student_assesment, student_final_exam)
letter_grade = grade_boundries(grade)

print(f"{student_name} got {grade} Which is a {letter_grade}")

