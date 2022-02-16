#!/usr/bin/env python3
"""
Using regex to obfuscate a log message
"""


from hashlib import new
from typing import List
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated:"""
    new_log = message
    for field in fields:
        new_log = re.sub(r'{}=.*?;'.format(field),
                         r'{}={};'.format(field, redaction), new_log)
    return re.sub(r';', separator, new_log)
