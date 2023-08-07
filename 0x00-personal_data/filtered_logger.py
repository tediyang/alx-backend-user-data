#!/usr/bin/env python3
"""
    a function filters personal data and encrypt them with the provided
    string.
"""
import re
from typing import List, Literal
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION: Literal = "***"
    FORMAT: Literal = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: Literal = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        intialize the constructor variables
        Args:
            fields (List[str]): the data to encrypt
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format the message
        Args:
            record (logging.LogRecord): the logged data

        Returns:
            str: new formatted message with logged attributes
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
