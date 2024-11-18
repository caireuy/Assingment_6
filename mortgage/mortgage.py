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

    ## ACCESSOR for loan_amount
    @property
    def loan_amount(self) ->float:
        """
        Accessor for the loan_amount attribute.
        Returns:
            float: value of the loan amount
        """
        return self.__loan_amount
    
    ## MUTATOR for loan_amount 
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

    ## ACCESSOR for Rate
    @property
    def rate(self) ->str:
        """
        Accessor for rate value
        
        Return:
            str: if the value provided is valid
        
        """

        return self.__rate
    
    ## MUTATOR for Rate
    @rate.setter
    def rate(self, value: str):
        """
        Rate value of mortgage

        Arg:
            value(str): value of rate
        Raises:
            ValueError: If the rate value is invalid
        """
        try:
            self.__rate = MortgageRate[value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")

        self.__loan_amount = value
    ## ACCESSOR for Frequency
    @property
    def frequency(self) -> str:
        """
        Accessor for Frequency value

        Returns:
            str: The number of payments per year string equivalent to enum value.       
        """
        return self.__frequency
    
    ## MUTATOR for Frequency
    @frequency.setter
    def frequency(self, value: str):
        """
        Frequency value for mortgage
        Arg:
            value(str): The number of payments per year string equivalent to enum value.
        Raises:
            ValueError: If the payment frequency value is invalid
        """
        try:
            self.__frequency = PaymentFrequency[value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        self.__frequency = value

    ## ACCESSOR for Amortization
    @property
    def amortization(self) -> int:
        """
        Accessor for amortization value
        Returns:
            int: The number of years to repay the mortgage loan
        """
        return self.__amortization
    
    @amortization.setter
    def amortization(self, value: int):
        """
        Amortization period for mortgage
        
        Arg:
            value(int): The number of years to repay the mortgage loan.
        Raises:
            ValueError: If amortization value is invalid
        """
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        
        self.__amortization = value

    # Calculated mortgage payment amount
    def calculate_payment(self) -> float:
        """
        Calculates the Weekly, biWeekly, or Monthly morthgage payment

        Return:
            float: calculated payment in to two decimal place.
        Values:
            P: Loan amount value
            i: interest rate/payment frequency
            n: amortization value * payment frequency
            M: calculation
        """
        P = self.loan_amount
        i = self.rate.value / self.frequency.value
        n = self.amortization * self.frequency.value

        M = P * (i * (1 + i)**n) / ((1 + i)**n - 1)
        
        return round(M, 2)