import pytest
from . import core_asserts


@pytest.fixture(scope="session")
def asserts():
    return core_asserts
