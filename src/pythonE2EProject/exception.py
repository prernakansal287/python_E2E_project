import sys
from src.pythonE2EProject.logger import logging

#this function is used to get the details of the error like in which file and in which line number the error occurred
#also its taken from 
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
    return error_message

#so here we are create a custom exception class 
#the custom exception class is "INHERITING" the properties of the base class Exception
#so that we can use the properties of the base class Exception in our custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Here we are calling the constructor of the base class Exception
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        detailed_error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {error_message}"
        return detailed_error_message

    def __str__(self):
        return self.error_message