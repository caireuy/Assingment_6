"""
Description: A class meant to manage Mortgage options.
Author: Carey Roxas
Date: Novemeber 10, 2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    Class to represent the MortgageRate, PaymentFrequency and the valid amortization

    MortgageRate: values of mortgage rate
    PaymentFrequency: payment frequency options
    VALID_AMORTIZATION: list of valid years for amortization
    """