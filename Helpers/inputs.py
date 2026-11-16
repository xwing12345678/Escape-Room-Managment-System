from .time_functs import get_current_date
from Validations.time_validations import past_year

def get_valid_year()->int:
    raw_choice = ""
    valid_year = False
    while not valid_year:
        raw_choice = input("Enter in the year you want to reserve: ")



    return int(raw_choice)