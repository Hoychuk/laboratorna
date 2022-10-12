MAX_STUDENTS = 20

import uuid


class Student:
    def __init__(self, new_name: str, new_surname: str, **new_grades):
        self.name = new_name
        self.surname = new_surname
        self.number = str(uuid.uuid4())
        self.grades = new_grades

    def __str__(self) -> str:
        return f"\n{self.surname} {self.name}: \nRecord book number: {str(self.number)}\
				 \nSubjects: {' '.join(map(str, self.grades))}\
				\nGrades: {' '.join(map(str, self.grades.values()))}\nAverage score: {str(self.average)} \n"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other) -> bool:
        return self.average < other.average

    def __gt__(self, other) -> bool:
        return self.average > other.average

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong data")
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong data")
        self.__surname = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not all (isinstance(i,int) for i in value.values() or not all(1 < i < 13 for i in value.values)):
            raise TypeError("Wrong data")
        self.__grades = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong data")
        self.__number = value

    @property
    def average(self):
        return sum(self.grades.values()) / len(self.grades)


class Group:
    def __init__(self, *args: Student):
        self.__list_of_students = []
        for student in args:
            self.append(student)

    @property
    def list_of_students(self):
        return self.__list_of_students

    def append(self, value):
        if not isinstance(value, Student):
            raise TypeError("Wrong data")
        if not self.__check(value) or not len(self.list_of_students) < MAX_STUDENTS:
            raise ValueError("There is already such student is group")
        self.__list_of_students += [value]

    def __check(self, student_to_check: Student) -> bool:
        for student in self.list_of_students:
            if student == student_to_check:
                return False
        return True

    def best_students(self) -> list:
        return sorted(self.list_of_students, reverse=True)[:5] if self.list_of_students else None


student1 = Student("s1", "t1", sub1=11, sub2=12)
student2 = Student("s2", "t2", sub1=7, sub2=8)
student3 = Student("s3", "t3", sub1=9, sub2=8)


group = Group(student1, student2,student3)

print("".join(map(str, group.best_students())))

