"""
Testing Configuration and Fixtures
"""

import random
from typing import List

import pytest


@pytest.fixture
def random_array() -> List[float]:
    """
    A random array of float objects

    Returns
    -------
    List[float]
    """
    length = 20
    return [random.uniform(0.0, 100.0) for i in range(length)]
