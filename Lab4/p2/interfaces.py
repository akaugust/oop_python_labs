from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplementedError

    @property
    @abstractmethod
    def teacher(self):
        raise NotImplementedError

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        raise NotImplementedError

    @property
    @abstractmethod
    def course_program(self):
        raise NotImplementedError

    @course_program.setter
    @abstractmethod
    def course_program(self, course_program):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ICourseFactory(ABC):

    @abstractmethod
    def insert_course(self, course_name, teacher_name, course_program, course_type):
        raise NotImplementedError

    @abstractmethod
    def insert_teacher(self, name):
        raise NotImplementedError

    @abstractmethod
    def select_all_teachers(self):
        raise NotImplementedError

    @abstractmethod
    def select_all_courses(self):
        raise NotImplementedError
