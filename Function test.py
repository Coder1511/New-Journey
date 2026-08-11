marks=[]
mark=""
for i in range(5):
    mark=int(input(f"Enter marks for subject_no {i+1}: "))
    while mark<0 or mark>100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        mark=int(input(f"Enter marks for subject_no {i+1}: "))
    marks.append(mark)
def get_grades(marks):
    grades=[]
    for mark in marks:
        if mark>=90:
            grades.append('A')
        elif mark>=80:
            grades.append('B')
        elif mark>=70:
            grades.append('C')
        elif mark>=60:
            grades.append('D')
        else:
            grades.append('F')
    return grades
print("Marks:", marks)
grades=get_grades(marks)
print("Grades:", grades)