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

    ##__INIT__
    def __init__(self, loan_amount: float,
                rate: str, 
                frequency: str, 
                amortization: int):
        """
        Initialize Mortgage validation with attributes: Loan amouunt, rate, frequency, amortization.

        Arg:
            Loan_amount(float): The amount of the mortgage loan.
            Rate(str): The annual interest rate string equivalent to enum value
            Frequency(str): The number of payments per year string equivalent to enum value.
            Amortization(int): The number of years to repay the mortgage loan.

        Raises:
            ValueError:  if the loan amount value is zero or negative
            ValueError: if the rate provided is invalid
            ValueError: if the frequency provided is invalid
            ValueError: if the amortization is invalid   
        """
        # Loan_amount validation

        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount
        
        # Rate Validation
        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        # Frequency Validation
        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        # Amortization Validation
        self.__amortization = amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")

    ## loan_amount ACCESSOR
    @property
    def loan_amount(self):
        """
        Accessor for the loan_amount attribute.
        Returns:
            float: value of the loan amount
        """
        return self.__loan_amount
    
    ## loan_amount MUTATOR
    @loan_amount.setter
    def loan_amount(self, value: float):
        """
        Mutator for loan_amount.

        Arg:
            value(float): Value of loan amount.
        Raises:
            ValueError: If the loan amount value is zero or negative
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = value

