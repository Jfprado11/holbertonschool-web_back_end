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
    new_log = message
    for field in fields:
        new_log = re.sub(r'({}=).*?;'.format(field),
                         r'\1{};'.format(redaction), new_log)
    return new_log
