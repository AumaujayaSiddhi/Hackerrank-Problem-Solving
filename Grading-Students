def gradingStudents(grades):
    for grade_index in range(len(grades)):
        diff = (5 - grades[grade_index] % 5)
        if grades[grade_index] > 37 and diff < 3:
            grades[grade_index] = grades[grade_index] + diff 
    return grades