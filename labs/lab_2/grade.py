"""
the GradeEntry class module.
"""


class GradeEntry:
    """Records the grade entries for a student record system.

    id - the course identifier string
    weight - the course weight (full year, half year)
    """

    id: str
    weight: float

    def __init__(self, id: str, weight: float) -> None:
        """ Initializes the class GradeEntry
        """

        self.id = id
        self.weight = weight

    def __str__(self):
        """ Provides a string representation of the grade entry
        """

        raise NotImplementedError('Subclass needed')

    def _invariant(self):
        """ Tests the condition
        """

        raise NotImplementedError('Subclass needed')

    def __eq__(self, other: 'GradeEntry'):
        """ Determines equality based on course id and weight for LetterGradeEntry
        """

        return (type(self) == type(other)
                and self.id == other.id
                and self.weight == other.weight)


class NumericGradeEntry(GradeEntry):
    """ Sub-class of grade-entry to handle numeric grades.
    """

    grade: int
    points: float

    def __init__(self, id: str, grade: int, weight: float) -> None:
        """ Initializes the NumericGradeEntry subclass and
        extends GradeEntry by adding:
        grade - numeric representation of grades
        points - grade point average
        """

        GradeEntry.__init__(self, id, weight)

        self.grade = grade

        self._invariant()
        if grade >= 85:
            self.points = 4.0
        elif grade >= 80:
            self.points = 3.7
        elif grade >= 77:
            self.points = 3.3
        elif grade >= 73:
            self.points = 3.0
        elif grade >= 70:
            self.points = 2.7
        elif grade >= 67:
            self.points = 2.3
        elif grade >= 63:
            self.points = 2.0
        elif grade >= 60:
            self.points = 1.7
        elif grade >= 57:
            self.points = 1.3
        elif grade >= 53:
            self.points = 1.0
        elif grade >= 50:
            self.points = 0.7
        else:
            self.points = 0.0

    def _invariant(self):
        # Tests the validity of the grade entered.
        assert 0 <= self.grade <= 100, 'Invalid number grade entry.'

    def __str__(self) -> str:
        """Representation of NumericGradeEntry
        """

        return 'Type: {}, Course: {}, Grade: {}, GPA: {}'.format(type(self).__name__,
                                                                 self.id,
                                                                 str(self.grade),
                                                                 str(self.points))


class LetterGradeEntry(GradeEntry):
    """ Sub-class of grade-entry to handle letter grades.
    """

    grade: str
    points: float

    def __init__(self, id: str, grade: int, weight: float) -> None:
        """ Initializes the NumericGradeEntry subclass and
        extends GradeEntry by adding:
        grade - letter representation of grades
        points - grade point average
        """

        GradeEntry.__init__(self, id, weight)

        self.grade = grade
        self._invariant()
        if grade == 'A+' or grade == 'A':
            self.points = 4.0
        elif grade == 'A-':
            self.points = 3.7
        elif grade == 'B+':
            self.points = 3.3
        elif grade == 'B':
            self.points = 3.0
        elif grade == 'B-':
            self.points = 2.7
        elif grade == 'C+':
            self.points = 2.3
        elif grade == 'C':
            self.points = 2.0
        elif grade == 'C-':
            self.points = 1.7
        elif grade == 'D+':
            self.points = 1.3
        elif grade == 'D':
            self.points = 1.0
        elif grade == 'D-':
            self.points = 0.7
        else:
            self.points = 0.0

    def _invariant(self):
        # tests validity of the letter grade entered
        l = ['A', 'A+', 'A-', 'B', 'B+', 'B-',
             'C', 'C+', 'C-', 'D', 'D+', 'D-', 'F']

        assert self.grade in l, 'Invalid letter grade entry'

    def __str__(self) -> str:
        """Representation of LetterGradeEntry
        """

        return 'Type: {}, Course: {}, Grade: {}, GPA: {}'.format(type(self).__name__,
                                                                 self.id,
                                                                 self.grade,
                                                                 str(self.points))

