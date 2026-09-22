import os
import sys
from Respire.Logger import logging

def error_message_detail(error, error_detail=None):
    if error_detail is not None and hasattr(error_detail, 'exc_info'):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        ermsg = f"Error in Script: {file_name} - Line: {exc_tb.tb_lineno} - Message: {str(error)}"
        logging.info(ermsg)
        return ermsg

    message = str(error)
    logging.info(message)
    return message


class CustomException(Exception):
    def __init__(self, ermsg, error_detail=None):
        super().__init__(ermsg)
        self.error_message = error_message_detail(ermsg, error_detail=error_detail)

    def __str__(self):
        return self.error_message