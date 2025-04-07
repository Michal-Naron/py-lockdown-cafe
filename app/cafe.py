from datetime import date
from app.errors import *

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cofe(self, visitor: dict):
        if  not "vaccine" in visitor.keys():
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"