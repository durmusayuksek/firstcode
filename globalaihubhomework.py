devam1 = False
for i in range(3):
    name = input('Please Enter Your First Name: ')
    surname = input('Please Enter Your Last Name: ')
    def harf1(name):
        return any(char.isalpha() for char in name)
    def harf2(surname):
        return any(char.isalpha() for char in surname)
    if harf1(name) and harf2(surname) == True:
        print('Welcome', name.upper(), surname.upper())
        devam1 = True
        break
    else:
        hak = 2 - i
        print('Invalid name or surname, you have', hak, 'attempts remaining.')
        if hak == 0:
            print('Please try later.')
if devam1:
    print('Welcome to the course selection page. You can choose a minimum of 3 and a maximum of 5 courses.')
    course = []
    devam2 = False
    while len(course) < 5:
        course1 = input('Please enter the course you would like to take (Press q to quit the course selection page): ')
        if len(course) < 3:
            if course1 == 'q':
                print("You haven't selected enough courses.")
                break
        else:
            if course1 == 'q':
                devam2 = True
                break
        course.append(course1)
    if len(course) < 3:
        print('You failed in class.')
    else:
        print('You have selected', course)
        devam2 = True
    if devam2:
        devam3 = True
        while devam3:
            exam = input(f'Which one of these {len(course)} courses would you like to choose to take an exam?: ')
            for i in course:
                if i == exam:
                    devam3 = False
                    break
                else:
                    if course.index(i) == len(course) - 1:
                        print('Invalid course selection for the exam')
        exam2 = exam.upper()
        devam4 = True
        while devam4:
            midterm = input(f'Enter your midterm exam score for the {exam2} course: ')
            if 0 <= int(midterm) <= 100:
                devam4 = False
            else:
                print('Invalid midterm score')
        devam5 = True
        while devam5:
            final = input(f'Enter your final exam score for the {exam2} course: ')
            if 0 <= int(final) <= 100:
                devam5 = False
            else:
                print('Invalid final score')
        devam6 = True
        while devam6:
            project = input(f'Enter your project score for the {exam2} course: ')
            if 0 <= int(project) <= 100:
                devam6 = False
            else:
                print('Invalid project score')
        grades = {}
        grades['midterm'] = int(midterm)
        grades['final'] = int(final)
        grades['project'] = int(project)
        print(f'Your scores for the {exam2} course are: {grades}')
        total = int(midterm) * 0.3 + int(final) * 0.5 + int(project) * 0.2
        exam_grade = 0
        if 90 <= total <= 100:
            exam_grade = 'AA'
        elif 70 <= total < 90:
            exam_grade = 'BB'
        elif 50 <= total < 70:
            exam_grade = 'CC'
        elif 30 <= total < 50:
            exam_grade = 'DD'
        else:
            exam_grade = 'FF'
        print(name.upper() + ' ' + surname.upper() + ',' + ' your total score for the', exam2,
              'course is', total, 'and your grade ise', exam_grade + '.')
