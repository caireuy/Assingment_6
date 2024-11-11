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

def MortgageRate(Enum):
    """
    Represents the Mortage rate values
    """

    FIXED_5: 0.0519
    """Fixed mortage rate 5th value"""

    FIXED_3: 0.0589
    """FIxed mortage rate 3rd value"""

    FIXED_1: 0.0599 
    """Fixed mortgage rate 1st value"""

    VARIABLE_5: 0.0649 
    """5th  variable for mortgage rate"""

    VARIABLE_3: 0.0669 
    """3rd variable for mortgage rate"""

    VARIABLE_1: 0.0679 
    """1st variable for mortgage rate"""
    
def PaymentFrequency(Enum):
    """
    Represents the payment frequency options
    """
    MONTHLY: 12
    """Monthly payment frequency of 12 times a year"""

    BI_WEEKLY: 26
    """Bi-weekly Payment frequemcy of 26 times a year"""

    WEEKLY: 52
    """Weekly payment frequency of 52 times a year"""
