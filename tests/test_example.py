"""
Example Assertions
"""

import logging

from fastapp._cli import root_logger as cli_logger


def test_math():
    """
    Do some Testing with Math
    """
    assert 1 + 1 == 2


def test_app_logging_level():
    """
    Assert Something on the App
    """
    assert cli_logger.level == logging.INFO
