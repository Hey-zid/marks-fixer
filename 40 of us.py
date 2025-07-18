with open ("40 of us.txt","r") as lines:
    lines_ = [line.strip().split(",") for line in lines]

the_id=int(input("Please give the student ID: "))
marks=int(input("Updated marks  "))

for i in range(len(lines_)):
    student_id = int(lines_[i][0])
    if student_id == the_id:
        lines_[i][2] = str(marks)

with open("40 of us.txt", "w") as file:
    for line in lines_:
        file.write(",".join(line) + "\n")

print("The Marks updated, Please check your file :)")