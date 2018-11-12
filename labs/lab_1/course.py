"""
Course class
"""
from typing import List


class Course:
    """A course class that students can add or drop.

    students - list of all student numbers enrolled
    limit - limit to how many students can add
    """

    students: List[str]
    limit: int

    def __init__(self, limit: int) -> None:
        """Initializes the course class
        """

        self.students = []
        self.limit = limit

    def change_limit(self, new_limit: int) -> None:
        """ Changes the number of students who can join the course.
        If the limit decreases, the students who enrolled the latest are kicked out.
        """
        if self.limit > new_limit:
            self.students = self.students[:new_limit]
        self.limit = new_limit

    def add(self, student_number: str) -> bool:
        """ Returns True and adds the student iff there is room.
        Return false otherwise
        """
        if len(self.students) < self.limit:
            self.students.append(student_number)
            return True
        else:
            return False

    def drop(self, student_number: str) -> bool:
        """ Returns True and drops the student iff they are in the course.
        Return False otherwise.
        """
        if student_number in self.students:
            self.students.remove(student_number)
            return True
        else:
            return False
