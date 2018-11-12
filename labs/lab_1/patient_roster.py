"""
Patient Roster module
"""

from typing import Dict, List

FAMILY_NAME = 0
FIRST_NAME = 1
GENDER = 2
MALE = 'MALE'

class PatientRoster:
    """An appointment system for a doctor's office.

    patients - a dictionary of key OHIP number containing the patient's
               family name, first name, and gender
    """

    balance: int
    limit: int
    male_patients: int
    female_patients: int

    def __init__(self, balance: int, limit: int) -> None:
        """ Initializes the PatientRoster class.
        """

        self.balance = balance
        self.limit = limit
        self.patients = {}

        self.male_patients = 0
        self.female_patients = 0

    def add_patient(self, ohip: str, family_name: str, first_name: str,
                    gender: str) -> bool:
        """ Returns True and adds a patient to the patient roster iff the doctor is
        not at their limit and it does not violate the difference and
        returns False otherwise."""

        if(ohip not in self.patients
           and abs(self.male_patients - self.female_patients) < self.balance
           and len(self.patients) < self.limit):
            self.patients[ohip] = [family_name, first_name, gender]
            if gender == MALE:
                self.male_patients += 1
            else:
                self.female_patients += 1
            return True
        else:
            return False
