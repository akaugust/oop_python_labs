from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, course_program):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):

    @abstractmethod
    def insert_course(self, course_name, teacher_name, course_program, course_type):
        pass

    @abstractmethod
    def insert_teacher(self, name):
        pass

    @abstractmethod
    def select_all_teachers(self):
        pass

    @abstractmethod
    def select_all_courses(self):
        pass
