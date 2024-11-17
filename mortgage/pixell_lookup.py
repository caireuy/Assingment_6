"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Carey Roxas
Date: November 10, 2024
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

class MortgageRate(Enum):
    """
    Represents the Mortgage rate values
    
    Values:
        FIXED_5: Fixed mortgage rate 5th value
        FIXEED_3: FIxed mortgage rate 3rd value
        FIXED_1: Fixed mortgage rate 1st value
        VARIABLE_5: 5th  variable for mortgage rate
        VARIABLE_3: 3rd variable for mortgage rate
        VARIABLE_1: 1st variable for mortgage rate     
    """

    FIXED_5: 0.0519

    FIXED_3: 0.0589

    FIXED_1: 0.0599 

    VARIABLE_5: 0.0649 

    VARIABLE_3: 0.0669 

    VARIABLE_1: 0.0679 
    
    
class PaymentFrequency(Enum):
    """
    Represents the payment frequency options
    
    Values:
        MONTHLY: Monthly payment frequency of 12 times a year
        BI_WEEKLY: Bi-weekly Payment frequency of 26 times a year
        WEEKLY: Weekly payment frequency of 52 times a year
    """
    MONTHLY: 12

    BI_WEEKLY: 26

    WEEKLY: 52
 
