from abc import ABC, abstractmethod


class ICourse:

    def __init__(self, name):
        self.name = name
        self.program = []
        self.teacher = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self.__name = value

    def add_topic(self, topic):
        if not isinstance(topic, str):
            raise TypeError()
        self.program.append(topic)

    def add_course_teacher(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError()
        self.teacher = teacher

    def __str__(self):
        string = '\n'.join(self.program)
        return f'Name: {self.name}\nTeacher: {self.teacher.name}\nProgram:\n{string}\n\n'


class ITeacher:

    def __init__(self, name):
        self.name = name
        self.courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self.__name = value

    def add_courses(self, course):
        if not isinstance(course, ICourse):
            raise TypeError()
        self.courses.append(course)

    def __str__(self):
        string = '\n'
        for i in self.courses:
            string += f'{i.name}\n'
        return f'Name: {self.name}\nCourses:{string}'


class ICourseFactory(ABC):

    @abstractmethod
    def add_course(self, name):
        pass

    @abstractmethod
    def add_teacher(self, name):
        pass

    @abstractmethod
    def create_course(self, teacher_name, course_names):
        pass


class CourseFactory(ICourseFactory):

    def __init__(self):
        self.teachers = []
        self.courses = []

    def add_course(self, name):
        if not isinstance(name, str):
            raise TypeError()
        course = ICourse(name)
        self.courses.append(course)

    def add_teacher(self, name):
        if not isinstance(name, str):
            raise TypeError()
        teacher = ITeacher(name)
        self.teachers.append(teacher)

    def create_course(self, teacher_name, course_names):
        if not isinstance(teacher_name, str):
            raise TypeError()
        for i in self.teachers:
            if teacher_name == i.name:
                teacher = i
                break
        for i in self.courses:
            for j in course_names:
                if j == i.name:
                    teacher.add_courses(i)
                    i.add_course_teacher(teacher)

    def __str__(self):
        string1 = f'\n'
        for i in self.teachers:
            string1 += f'{i.name}\n'
        string2 = f'\n'
        for i in self.courses:
            string2 += f'{i.name}\n'
        return f'Teachers:{string1}\nCourses:{string2}'


class CourseLocation(ABC):

    @abstractmethod
    def location(self, course):
        pass


class ILocalCourse(CourseLocation):

    def location(self, course, lab):
        if not isinstance(course, CourseFactory):
            raise TypeError()
        if not isinstance(lab, str):
            raise TypeError()
        course.location = lab
        print(f'Location: {course.location}')


class IOffsiteCourse(CourseLocation):

    def location(self, course, city):
        if not isinstance(course, CourseFactory):
            raise TypeError()
        if not isinstance(city, str):
            raise TypeError()
        course.location = city
        print(f'Location: {course.location}')


courses = CourseFactory()
courses.add_course('OOP')
courses.add_course('Database')
courses.courses[0].add_topic('Encapsulation')
courses.courses[0].add_topic('Inheritance')
courses.courses[0].add_topic('Polymorphism')
courses.courses[1].add_topic('SELECT statement')
courses.courses[1].add_topic('WHERE statement')
courses.add_teacher('Tymchuk')
courses.add_teacher('Datsiuk')
courses.create_course('Tymchuk', ['OOP'])
courses.create_course('Datsiuk', ['Database'])
print(courses.teachers[0])
print(courses.courses[0])
print(courses.courses[1])
location = ILocalCourse()
print(courses)
location.location(courses, 'Kyiv')