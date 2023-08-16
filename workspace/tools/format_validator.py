"""
This script is used to validate the input dataset file format by the user.
"""

# Required Libararies & Packages
import pandas as pd
import requests

# Define Validator Class

## CSV Validator Class
class CSVValidator:
    
    @staticmethod
    def is_valid(file_path):
        # Implement CSV-Specific validation logic
        try:
            # Read the input csv file 
            pd.read_csv(file_path)
            
            return True
        
        # Catch the exception error
        except Exception as e:
            
            print(f'Invalid CSV file: {e}')

            return False
        

## Excel Validator Class
class ExcelValidator:

    @staticmethod
    def is_valid(file_path):
        # Implement Excel-Specific validation logic
        try:
            # Read the input excel file
            pd.read_excel(file_path)

            return True
        
        # Catch the exception error
        except Exception as e:

            print(f"Invalid Excel file: {e}")

            return False


## API Validator Class
class APIValidator:

    @staticmethod
    def is_valid(api_url):
        # Implement API-Specific validation logic
        try:
            # Read the input excel file
            response = requests.head(api_url)

            return response.status_code == 200
        
        # Catch the exception error
        except Exception as e:

            print(f"Invalid API URL: {e}")

            return False


# Define Validator Factory
def get_validator(data_source_type):

    if data_source_type == 'csv':
        return CSVValidator
    
    elif data_source_type == 'excel':
        return ExcelValidator
    
    elif data_source_type == 'api':
        return APIValidator
    
    else:
        raise ValueError('Unsupported data source format')
    

# Define Validation Process
def validate_data_source(data_source_type, source_path_or_url):
    validator = get_validator(data_source_type)
    return validator.is_valid(source_path_or_url)
