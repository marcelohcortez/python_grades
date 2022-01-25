import os

def grades():
    decision = input('Do you want to INSERT STUDENTS (insert), VIEW STUDENTS (view), GRADE STUDENTS (grade) or CALCULATE THE GRADES (calculate)?\n').lower()

    if decision == 'insert':
        students_insert()
    elif decision == 'view':
        students_view()
    elif decision == 'grade':
        students_grade()
    elif decision == 'calculate':
        students_calculate()
    else:
        print('That is not a valid option. Try again.\n')
        grades()


def students_insert():
    i = 0
    students_total = int(input('How many students you want to insert?\n'))

    while i < students_total:
        student_name = input('Please, insert student first and last name:\n')
        with open('students_list.txt', 'a') as file:
            file.write(f'{student_name}\n')
        i+=1
    
    grades()

def students_view():
    decision = input('Do you want to view the students who PASSED (passed), the students who DIDN\'T PASSED (failed), or do you wanto to LIST ALL STUDENTS (listall)?\n').lower()

    if decision == 'passed':
        if os.path.exists("students_passed.txt"):
            with open('students_passed.txt', 'r') as file:
                for line in file.readlines():
                    student_name = line.rstrip()
                    print(f'{student_name}\n')
        else:
            print('The list doesn\'t exist yet. Please generate it first\n')
            students_view()
    elif decision == 'failed':
        if os.path.exists("students_failed.txt"):
            with open('students_failed.txt', 'r') as file:
                for line in file.readlines():
                    student_name = line.rstrip()
                    print(f'{student_name}\n')
        else:
            print('The list doesn\'t exist yet. Please generate it first\n')
            students_view()
    elif decision == 'listall':
        if os.path.exists("students_list.txt"):
            with open('students_list.txt', 'r') as file:
                for line in file.readlines():
                    student_name = line.rstrip()
                    print(f'{student_name}\n')
        else:
            print('The list doesn\'t exist yet. Please generate it first\n')
            students_view()
    else:
        print('That is not a valid option. Try again.\n')
        students_view()
    
    students_view()

def students_grade():
    print('\nATTENTION: Please, remember that each grade must not be lower than 0 nor higher than 10\n')
    
    with open('students_list.txt', 'r') as file:
        for line in file.readlines():
            student_name = line.rstrip()
            student_first_grade = float(input(f'What is the first grade for {student_name}?\n'))
            student_second_grade = float(input(f'What is the second grade for {student_name}?\n'))
            with open('students_grades.txt', 'a') as file:
                file.write(f'{student_name}:{student_first_grade}:{student_second_grade}\n')
    
    decision = input('All grades inserted. Do you want to calculate the final grades? (Y/N)').lower()

    if decision == 'y':
        students_calculate()
    elif decision == 'n':
        grades()
    else:
        print('That is not a valid option. Try again.\n')
        decision = input('All grades inserted. Do you want to calculate the final grades? (Y/N)').lower()

    grades()

def students_calculate():
    decision = input('\nATTENTION: Do you confirm that you want to generate the lists with the students who passed and the ones that failed?\
        This will remove the previous result files and generate new ones. (Y/N)?\n')

    if decision == 'y':
        with open('students_grades.txt', 'r') as file:
            for line in file.readlines():
                student_info = line.rstrip()
                student_name, student_first_grade, student_second_grade  = student_info.split(":")
                student_final_grade = round((float(student_first_grade) + float(student_second_grade)) / 2, 2)

                if student_final_grade >= 7.0:
                    with open('students_passed.txt', 'a') as file:
                        file.write(f'{student_name}:{student_final_grade}\n')
                else:
                    with open('students_failed.txt', 'a') as file:
                        file.write(f'{student_name}:{student_final_grade}\n')
        
        view_results = input('Lists generated. Do you want to view the results? (Y/N)\n').lower()

        if view_results == 'y':
            students_view()
        elif view_results == 'n':
            grades()
        else:
            print('That is not a valid option. Try again.\n')
            view_results = input('Lists generated. Do you want to view the results? (Y/N)\n').lower()

    elif decision == 'n':
        grades()
    else:
        print('That is not a valid option. Try again.\n')
        students_calculate()

if __name__ == '__main__':
    grades()