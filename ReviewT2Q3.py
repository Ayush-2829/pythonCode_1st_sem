# Program Name: Grade System
# Program Purpose: Enter and display grades for 5 students
# Program author: Hugo Strange
# Date completed: 11.5.24

# Declare variables
studentGrades = {}

# Intro
print('Welcome to our grading system')

# Get 5 students and their 2 grades
for num in range(1,6):
    studentName = input('Please enter the student\'s name: ').strip().title()

    grades = []
    for grade in range(1,3):
        mark = input(f'Please enter grade #{grade}: ').strip()
        mark = float(mark)
        grades.append(mark)

    studentGrades[studentName] = grades

print('Here are the results:')


# Show the output
for studentName, grades in studentGrades.items():
    nameLenght = len(studentName)
    print(studentName)
    print('_'*nameLenght)

    for index,grade in enumerate(grades):
        print(f'For test#{index+1}: {grade:.1f}%')
    
print('Thanks for using this program')



