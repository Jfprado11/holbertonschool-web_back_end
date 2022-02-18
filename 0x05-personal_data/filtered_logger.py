#!/usr/bin/env python3
"""
Using regex to obfuscate a log message
"""


from hashlib import new
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated:"""
    for field in fields:
        message = re.sub(r'({}=).*?;'.format(field),
                         r'\1{}{}'.format(redaction, separator), message)
    return message
