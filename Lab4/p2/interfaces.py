from abc import ABC, abstractmethod


class ITeacher(ABC):
    """
    Abstract Class for the Teachers
    Implements ABC

    Attributes:
    --------
    name : str
    abstract name of teacher

    Abstract Methods:
    ------
    def name(self):
        name getter
    def name(self, name):
        name setter
    def __str__(self):
        prints objects in string form
    """

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
    """
    Abstract Class for the Courses
    Implements ABC

    Attributes:
    --------
    name : str
        abstract name of the Course
    teacher_name : Teacher
        abstract Teacher object
    course_program : str
        abstract course program

    Abstract Methods:
    ------
    def name(self):
        name getter
    def name(self, name):
        name setter
    def teacher_name(self):
        teacher getter
    def teacher_name(self, teacher_name):
        teacher setter
    def course_program(self):
        course_program getter
    def course_program(self, course_program):
        course_program setter
    def __str__(self):
        prints objects in string form
    """
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
    """
    Abstract Class for the Local Courses
    Implements ABC

    Attributes:
    --------
    name : str
        Abstract name of the Course
    teacher_name : Teacher
        Abstract Teacher object
    course_program : str
         Abstract course program

    Abstract Methods:
    ------
    def __str__(self):
        prints objects in string form
    """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class IOffsiteCourse(ABC):
    """
    Abstract Class for the Offsite Courses
    Implements ABC

    Attributes:
    --------
    name : str
        Abstract name of the Course
    teacher_name : Teacher
        Abstract Teacher object
    course_program : str
        Abstract course program

    Abstract Methods:
    ------
    def __str__(self):
        prints objects in string form
    """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ICourseFactory(ABC):
    """
    Abstract Class for the Offsite Courses
    Implements ABC

    Attributes:
    --------
    None

    Abstract Methods:
    ------
    def connect():
        connects to database
    def insert_course(self, course_name, teacher_name, course_program, course_type):
        adds new Course
    def insert_teacher(self, name):
        adds new Teacher
    def select_all_teachers(self):
        selects all Teachers from database
    def select_all_courses(self):
        selects all Courses from database
    """

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
