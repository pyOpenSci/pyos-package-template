# -*- coding: utf-8 -*-
"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import random

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100),10)


def test_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = {{ cookiecutter.project_slug }}.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


def test_max_number(generate_numbers)
    """Sample test function for max_number, using pytest fixture."""

    our_result = {{ cookiecutter.project_slug }}.max_numbers(generate_numbers)
    assert our_result == max(generate_numbers)


def test_max_number_bad(generate_numbers)
    """Sample test function that should fail."""

    our_result = {{ cookiecutter.project_slug }}.max_numbers(generate_numbers)
    assert our_result == max(generate_numbers) + 1
