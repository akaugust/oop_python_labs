from abc import ABC

from interfaces import ICourse, ITeacher, ILocalCourse, IOffsiteCourse, ICourseFactory

import pymysql
from config import host, user, password, database


class Teacher(ITeacher):

    teachers_courses = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """Name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of teacher name!")
        if not name or name.__contains__(" "):
            raise ValueError("Wrong value of teacher name!")
        self.__name = name

    def __str__(self):
        return f'Teacher - {self.name}'


class Course(ICourse, ABC):

    def __init__(self, name, teacher_name, course_program):
        self.name = name
        self.teacher_name = teacher_name
        self.course_program = course_program

    @property
    def name(self):
        """Name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of course name!")
        if not name or name.__contains__(" "):
            raise ValueError("Wrong value of course name!")
        self.__name = name

    @property
    def teacher_name(self):
        """teacher getter"""
        return self.__teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        """teacher setter"""
        if not isinstance(teacher_name, Teacher):
            raise TypeError("Wrong type of teacher!")
        self.__teacher_name = teacher_name

    @property
    def course_program(self):
        """course_program getter"""
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        """Name setter"""
        if not isinstance(course_program, str):
            raise TypeError("Wrong type of course_program!")
        if not course_program:
            raise ValueError("Wrong value of course_program!")
        self.__course_program = course_program

    def __str__(self):
        return f'Course: {self.name}\n Teacher: {self.teacher_name}\n Course program: {self.course_program}'


class LocalCourse(Course, ILocalCourse, ABC):

    def __init__(self, name, teacher_name, course_program):
        super().__init__(name, teacher_name, course_program)
        self.course_type = "Local"

    def __str__(self):
        return super().__str__() + 'Type: Local\n'


class OffsiteCourse(Course, IOffsiteCourse, ABC):

    def __init__(self, name, teacher_name, course_program):
        super().__init__(name, teacher_name, course_program)
        self.course_type = "Offsite"
    
    def __str__(self):
        return super().__str__() + 'Type: Offsite\n'


class CourseFactory(ICourseFactory):

    def __init__(self):
        self.connection = CourseFactory.connect()

    @staticmethod
    def connect():
        connector = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        return connector

    def insert_course(self, course_name, teacher_name, course_program, course_type):
        insert_id = 0
        teachers_list = self.select_all_teachers()
        if teacher_name.name not in teachers_list.values():
            raise ValueError("No Teachers like this!")
        for id, name in teachers_list.items():
            if name == teacher_name.name:
                insert_id = id
        with self.connection.cursor() as cursor:
            insert_new_course = 'INSERT INTO course (course_name, teacher_id, course_program, course_type) ' \
                                 'VALUES (%s, %s, %s, %s)'
            cursor.execute(insert_new_course, (course_name, insert_id, course_program, course_type))
            self.connection.commit()
        if course_type == "local":
            return LocalCourse(course_name, teacher_name, course_program)
        elif course_type == "offsite":
            return OffsiteCourse(course_name, teacher_name, course_program)

    def insert_teacher(self, name):
        with self.connection.cursor() as cursor:
            insert_new_teacher = 'INSERT INTO teacher (teacher_name) VALUES (%s)'
            cursor.execute(insert_new_teacher, (name,))
            self.connection.commit()
        return Teacher(name)

    def select_all_teachers(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM teacher')
            return dict(cursor.fetchall())

    def select_all_courses(self):
        with self.connection.cursor() as cursor:
            select_teachers = 'SELECT course.course_name, teacher.teacher_name, course.course_program, course.course_type ' \
                              'FROM course ' \
                              'JOIN teacher ON course.teacher_id = teacher.id'
            cursor.execute(select_teachers)
            return cursor.fetchall()


if __name__ == '__main__':
    factory = CourseFactory()
    teacher_A = CourseFactory().insert_teacher("A")
    teacher_B = CourseFactory().insert_teacher("B")
    course1 = CourseFactory().insert_course('OOP', teacher_A, 'Offsite', 'Database and abstract classes')
    course2 = CourseFactory().insert_course('OOP', teacher_A, 'Local', 'Database and abstract classes')
    course3 = CourseFactory().insert_course('Database', teacher_B, 'Local', 'Database and abstract classes')
    print(factory.select_all_teachers())
    print(factory.select_all_courses())
