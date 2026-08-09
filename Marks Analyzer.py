print("Please enter the marks for 5 subjects (between 0 and 100): ")
marks=[]
subject_no=list(range(1,6))
mark=""
for i in subject_no:
    mark=int(input("Enter marks for subject {}: ".format(i)))
    while mark < 0 or mark > 100:
        print("Invalid marks entered. Please enter marks between 0 and 100.")
        mark=int(input("Enter marks for subject {}: ".format(i)))
    else:
        marks.append(mark)
print()
for i in subject_no:
    print("Marks for subject {}: {}".format(i, marks[i-1]))
print("\n")
print("----- Results ----- ")
print("Marks: {}".format(marks))
print("Total Marks: {}".format(sum(marks)))
print("Average Marks: {}".format(sum(marks)/len(marks)))
print("Highest Marks: {}".format(max(marks)))
print("Lowest Marks: {}".format(min(marks)))
print("\n")