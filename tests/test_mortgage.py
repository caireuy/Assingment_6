"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    """
    Unit tests for the Mortgage class.
    1. A test case to ensure that the __init__() raises a ValueError when an invalid amount input value is used.
    2. A test case to ensure that the __init__() raises a ValueError when an invalid rate input value is used.
    3. A test case to ensure that the __init__() raises a ValueError when an invalid frequency input value is used.
    4. A test case to ensure that the __init__() raises a ValueError when an invalid amortization input value is used.
    5. A test case to ensure that the __init__() properly sets the attributes when valid inputs are provided.
    """

    # 1
    def test_init_loan_amount_invalid_amount(self):
        
        # Arrange
        loan_amount = 0 # Invalid Input
        rate = "FIXED_5"
        frequency = "BI_WEEKLY"
        amortization = 5
            
        # Act
        with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")
        
    # 2
    def test_init_rate_invalid_value(self):
         
         # Arrange
        loan_amount = 10000
        rate = "INVALID" # Invalid input
        frequency = 12
        amortization = 5
        
        expected = "Rate provided is invalid."
         # Act
        with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, rate, frequency, amortization)
        
         # Assert
        self.assertEqual(expected, str(context.exception))
      
        
    
    # 3 
    def test_init_frequency_invalid_value(self):
          
          # Arrange
        loan_amount = 10000
        rate = "FIXED_5" 
        frequency = "INVALID"  # Invalid input
        amortization = 5

        expected = "Frequency provided is invalid."
          # Act
        with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, rate, frequency, amortization)
            
          # Assert
        self.assertEqual(expected, str(context.exception))
      
     
    #4
    def test_init_amortization_invalid_value(self):
          
        # Arrange
        loan_amount = 10000
        rate = "FIXED_5" 
        frequency = "BI_WEEKLY"
        amortization = 40 # Invalid Input
        # Act
        with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, rate, frequency,amortization)

        # Assert
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")
    #5
    def test_init_all_valid_inputs(self):
         # Arrange
        loan_amount = 5000
        rate = "FIXED_5"
        frequency = "MONTHLY"
        amortization = 5

        # ACT
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(mortgage._Mortgage__loan_amount, loan_amount)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__amortization, amortization)

    """
    Test Case of Loan Amount Accessor and Mutators.
    1. Modify the Loan Amount to a negative value and verify results.
    2. Modify the Loan Amount to zero and verify results.
    3. Modify the Loan Amount to a positive value and verify results.
    """
    #1
    def test_loan_amount_negative_value(self):
        # Arrange
      loan_amount = -10
      rate = "FIXED_5" 
      frequency = "BI_WEEKLY"
      amortization = 10
       
      

        # Act
      with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
      self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    #2
    def test_loan_amount_zero_value(self):
        # Arrange
      loan_amount = 0
      rate = "FIXED_5" 
      frequency = "BI_WEEKLY"
      amortization = 10
        # Act
      with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
      self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    #3
    def test_loan_amount_positive_value(self):
      # Arrange
      loan_amount = 5000
      rate = "FIXED_5" 
      frequency = "BI_WEEKLY"
      amortization = 10

      # Act
      mortgage = Mortgage(loan_amount, rate, frequency, amortization)

      # Assert
      self.assertEqual(mortgage._Mortgage__loan_amount, loan_amount)

    """
    Test case for Rate Accessor and Mutator

    1. Modify the Rate to one of the possible MortgageRate enum values and verify results.
    2. Modify the Rate to a value that is not of MortgageRate enum type and verify results.
    """

    #1
    def test_rate_valid_rate_value(self):
        # Arrange
      loan_amount = 5000
      rate = "FIXED_5" 
      frequency = "BI_WEEKLY"
      amortization = 10

      
        # Act
      mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
      self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
    
    #2
    def test_rate_invalid_rate_value(self):
      # Arrange
      loan_amount = 5000
      rate = "INVALID" 
      frequency = "BI_WEEKLY"
      amortization = 10
      
      expected = "Rate provided is invalid."
      # Act
      with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
      # Assert
      self.assertEqual(expected, str(context.exception))
