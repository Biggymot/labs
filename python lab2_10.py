class Student():
    name = ""
    age = 18
    avr_score = 0
    faculty = "CompSci"
    professor = ""

    def __init__(self, name, age, avr_score):
        self.name = name
        self.age = age
        self.avr_score = avr_score

    def set_name(self, new_name):
        self.name = new_name

    def print_name(self, greeting):
        print greeting, self.name

    def print_age(self, age_text):
        print self.name, age_text, self.age

    def print_faculty(self, faculty_text):
        print self.name, faculty_text, self.faculty

    def print_avr_score(self, avr_score_text):
        print self.name, avr_score_text, self.avr_score

    # def print_

# <Name>'s age is <age>
st1 = Student("Mary", 20, 5)
# st1.name = "Mary"
# st1.age = 20
# st1.avr_score = 5

st1.print_age("'s age is")
st1.print_faculty("'s faculty is")
st1.print_avr_score('s average score is')
#print st1.name

st1.print_name("Hello,")
st1.set_name("Mary Poppins")
st1.print_name("Hello,")
print st1.age
print st1.faculty

st2 = Student("Bill", 18, 2)
#st2.name = "Bill"
st2.faculty = 'physics'
# st2.avr_score = 2
st2.print_age("'s age is")
st2.print_faculty("'s faculty is")
st2.print_avr_score('s average score is')
#print st2.name
st2.print_name("Hello,")
print st2.age


class Professor():
    name = "Donald Smith"
    year_salary = 1000
    hire_date = 1980
    birth_date = 1952
    faculty = "Biology"
    student_lst = []

    def print_salary(self, salary_text):
        print self.name, salary_text, self.year_salary

    def print_faculty(self, faculty_text):
        print self.name, faculty_text, self.faculty

    def print_age_when_hired(self, hire_text):
        print self.name, hire_text, (self.hire_date - self.birth_date)

    def print_list_of_students(self, student_text):
        print self.name, student_text, self.student_lst

prof1 = Professor()
prof1.print_salary(':')
prof1.print_faculty('from')
prof1.print_age_when_hired('from')


st1.professor = prof1
prof1.name = "Will Smith"
prof1.student_lst.append(st2.name)
prof1.student_lst.append(st1.name)
prof1.print_list_of_students('are')

prof2 = Professor()
prof2.name = "John Rendel"
st2.professor = prof2

prof3 = Professor()
prof3.name = "Donald Trump"
st2.professor = prof3

st2.professor.print_age_when_hired('from')
print st1.professor.print_salary(" = ")



