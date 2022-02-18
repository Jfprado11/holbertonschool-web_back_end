#!/usr/bin/env python3
"""
Using regex to obfuscate a log message
"""


import logging
from typing import List
import re


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """iniatilize the class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """gets the format of a log
        """
        message_obfs = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = message_obfs.replace(";", "; ")
        format_msg = logging.Formatter(self.FORMAT)
        return format_msg.format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated:"""
    for field in fields:
        message = re.sub(r'({}=).*?{}'.format(field, separator),
                         r'\1{}{}'.format(redaction, separator), message)
    return message
