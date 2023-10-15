class Student:

  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.student_grades = {}

  def add_courses(self, course_name):
    self.finished_courses.append(course_name)

  def rate_lecturer(self, lecturer, course_name, rate):
    if (isinstance(lecturer, Lecturer) 
        and course_name in lecturer.courses_attached 
        and course_name in self.finished_courses 
        or course_name in self.courses_in_progress):
      if course_name in lecturer.grades:
        lecturer.grades[course_name] += [rate]
      else:
        lecturer.grades[course_name] = [rate]
    else:
      print('Error from rate_lecturer function')

  def av_grade_student(self):
    total_sum = 0
    total_count = 0
    for x in self.student_grades:
      total_sum += sum(self.student_grades[x])
    for y in self.student_grades:
      total_count += len(self.student_grades[y])
    return float("{:.1f}".format(total_sum / total_count))
  
  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade_student()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    return res

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Not a Student')
      return
    return self.av_grade_student() < other.av_grade_student()

class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

  
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def av_grade(self):
    total_sum = 0
    total_count = 0
    for x in self.grades:
      total_sum += sum(self.grades[x])
    for y in self.grades:
      total_count += len(self.grades[y])
    return float("{:.1f}".format(total_sum / total_count))
      
  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade()}'
    return res

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Not a Lecturer')
      return
    return self.av_grade() < other.av_grade()

class Reviewer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
  
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in student.courses_in_progress:
      if course in student.student_grades:
        student.student_grades[course] += [grade]
      else:
        student.student_grades[course] = [grade]
    else:
      return 'Error'

  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}'
    return res
    

  
# Creating the instances of Student class  
student_alex = Student('alex', 'gayduk', 'male')
student_ema = Student('ema', 'ivanova', 'female')

student_alex.finished_courses += ['Git']
student_alex.courses_in_progress += ['Python', 'Java']
student_alex.student_grades['Git'] = [10, 8, 6]
student_alex.student_grades['Python'] = [6, 9, 9]

student_ema.finished_courses += ['Python']
student_ema.courses_in_progress += ['Git']
student_ema.student_grades['Git'] = [2, 5, 9]
student_ema.student_grades['Python'] = [8, 8, 6]

# Creating the instances of Lecturer class  
oleg_lecturer = Lecturer('Oleg', 'Bautin')
vlad_lecturer = Lecturer('Vlad', 'Ivanov')

oleg_lecturer.courses_attached += ['Java', 'Python', 'C++', 'Git']
vlad_lecturer.courses_attached += ['Python', 'Git']

print(f'Oleg lecturer courses attached: {oleg_lecturer.courses_attached}\nVlad lecturer courses attached: {vlad_lecturer.courses_attached}', '\n','----')


student_alex.rate_lecturer(oleg_lecturer, 'Git', 5)
student_alex.rate_lecturer(oleg_lecturer, 'Python', 6)
student_alex.rate_lecturer(vlad_lecturer, 'Git', 3)
student_alex.rate_lecturer(vlad_lecturer, 'Python', 2)

student_ema.rate_lecturer(oleg_lecturer, 'Git', 3)
student_ema.rate_lecturer(oleg_lecturer, 'Python', 7)
student_ema.rate_lecturer(vlad_lecturer, 'Git', 6)
student_ema.rate_lecturer(vlad_lecturer, 'Python', 9)

cool_reviewer = Reviewer('David', 'Sidorov')
cool_reviewer.rate_hw(student_alex, 'Python', 7)

print('Student Alex. Finished courses:', student_alex.finished_courses, end='\n')
print('Student Alex. Courses in progress:', student_alex.courses_in_progress, end='\n')
print(f'Student Alex.Grates: {student_alex.student_grades}')
print(f'Student Ema.Grates: {student_ema.student_grades}')
print(f'Oleg lecturer grades: {oleg_lecturer.grades}')

print('----')

print('Student details:', end='\n')
print(student_alex, '\n','----')
print(student_ema, '\n','----')
print(oleg_lecturer, '\n','----')
print(vlad_lecturer, '\n','----')
print(cool_reviewer, '\n','----')

print(oleg_lecturer < vlad_lecturer)
print(oleg_lecturer > vlad_lecturer)
print(student_alex > student_ema)

student_group = [student_alex, student_ema]

def av_rate_group(student_group_list, course_name):
  list_of_grades = []
    
  for student in student_group_list:
    if course_name in student.student_grades:
      list_of_grades += student.student_grades[course_name]
    else:
      return 'Error'
  print(float("{:.1f}".format(sum(list_of_grades) / len(list_of_grades))))

av_rate_group(student_group, 'Git')

lectorer_group = [oleg_lecturer, vlad_lecturer]

def av_rate_lectorer_group(lectorer_group_list, course_name):
  list_of_grades = []
    
  for lectorer in lectorer_group_list:
    if course_name in lectorer.grades:
      list_of_grades += lectorer.grades[course_name]
    else:
      return 'Error'
  print(float("{:.1f}".format(sum(list_of_grades) / len(list_of_grades))))

av_rate_lectorer_group(lectorer_group, 'Git')