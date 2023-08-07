#!/usr/bin/env python3
"""
    a function filters personal data and encrypt them with the provided
    string.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str):
    """
    filter and encrypt the data in the field
    Args:
        fields (List[str]): a list of strings representing all fields to
        obfuscate.
        redaction (str): a string representing by what the field will be
        obfuscated.
        message (str): a string representing the log line.
        separator (str): a string representing by which character is
        separating all fields in the log line (message).
    """
    for key in fields:
        message = re.sub(r"({}=)[^{}]+".format(key, separator),
                         r"\1{}".format(redaction), message)
    return message
