print("Please enter the marks for 5 subjects (between 0 and 100): ")
marks=[]
subject_no = range(1, 6)
for i in subject_no:
    mark=int(input(f"Enter marks for subject {i}: "))
    while mark < 0 or mark > 100:
        print("Invalid marks entered. Please enter marks between 0 and 100.")
        mark=int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
print()
for i in subject_no:
    print(f"Marks for subject {i}: {marks[i-1]}")
print("\n")
print("----- Results ----- ")
print(f"Marks: {marks}")
print(f"Total Marks: {sum(marks)}")
print(f"Average Marks: {sum(marks)/len(marks)}")
print(f"Highest Marks: {max(marks)}")
print(f"Lowest Marks: {min(marks)}")
print("\n")