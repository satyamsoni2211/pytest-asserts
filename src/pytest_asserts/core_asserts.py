import io
import inspect
import pytest
from .utils import raise_assertion_error


def assert_true(value):
    """Assert that the value is True."""
    if not value:
        raise_assertion_error(f"{value} is Falsy")


def assert_false(value):
    """Assert that the value is False."""
    if value:
        raise_assertion_error(f"{value} is Truthy")


def assert_equal(expected, actual):
    """Assert that the expected value is equal to the actual value."""
    if expected != actual:
        raise_assertion_error(f"{expected} and {actual} are not equal")


def assert_not_equal(expected, actual):
    """Assert that the expected value is not equal to the actual value."""
    if expected == actual:
        raise_assertion_error(f"{expected} and {actual} are equal")


def assert_in(expected, actual):
    """Assert that the expected value is in the actual value."""
    if expected not in actual:
        raise_assertion_error(f"{expected} is not in {actual}")


def assert_not_in(expected, actual):
    """Assert that the expected value is not in the actual value."""
    if expected in actual:
        raise_assertion_error(f"{expected} is in {actual}")


def assert_is_instance(expected, actual):
    """Assert that the actual value is an instance of the expected value."""
    if not isinstance(actual, expected):
        raise_assertion_error(f"{actual} is not an instance of {expected}")


def assert_is_not_instance(expected, actual):
    """Assert that the actual value is not an instance of the expected value."""
    if isinstance(actual, expected):
        raise_assertion_error(f"{actual} is an instance of {expected}")


def assert_is_none(value):
    """Assert that the value is None."""
    if value is not None:
        raise_assertion_error(f"{value} is not None")


def assert_is_not_none(value):
    """Assert that the value is not None."""
    if value is None:
        raise_assertion_error(f"{value} is None")


def assert_raises(exception, func, *args, **kwargs) -> pytest.ExceptionInfo:
    """Assert that the function raises an exception."""
    with pytest.raises(exception) as e:
        func(*args, **kwargs)
    return e


def assert_raises_message(exception, message, func, *args, **kwargs) -> pytest.ExceptionInfo:
    """Assert that the function raises an exception with the given message."""
    with pytest.raises(exception, match=message) as e:
        func(*args, **kwargs)
    return e


def assert_length(expected, actual):
    """Assert that the actual value has the expected length."""
    if len(actual) != expected:
        raise_assertion_error(f"{actual} has a length of {len(actual)}, not {expected}")


def assert_greater_than(expected, actual):
    """Assert that the actual value is greater than the expected value."""
    if actual <= expected:
        raise_assertion_error(f"{actual} is not greater than {expected}")


def assert_greater_than_or_equal(expected, actual):
    """Assert that the actual value is greater than or equal to the expected value."""
    if actual < expected:
        raise_assertion_error(f"{actual} is not greater than or equal to {expected}")


def assert_less_than(expected, actual):
    """Assert that the actual value is less than the expected value."""
    if actual >= expected:
        raise_assertion_error(f"{actual} is not less than {expected}")


def assert_less_than_or_equal(expected, actual):
    """Assert that the actual value is less than or equal to the expected value."""
    if actual > expected:
        raise_assertion_error(f"{actual} is not less than or equal to {expected}")


def assert_almost_equal(expected, actual, places=7):
    """Assert that the actual value is almost equal to the expected value."""
    if round(expected - actual, places) != 0:
        raise_assertion_error(f"{actual} is not almost equal to {expected}")


def assert_is(expected, actual):
    """Assert that the actual value is the expected value."""
    if expected is not actual:
        raise_assertion_error(f"{actual} is not {expected}")


def assert_is_subclass(expected, actual):
    """Assert that the actual value is a subclass of the expected value."""
    if not issubclass(actual, expected):
        raise_assertion_error(f"{actual} is not a subclass of {expected}")


def assert_not_is_subclass(expected, actual):
    """Assert that the actual value is not a subclass of the expected value."""
    if issubclass(actual, expected):
        raise_assertion_error(f"{actual} is a subclass of {expected}")


def assert_is_not(expected, actual):
    """Assert that the actual value is not the expected value."""
    if expected is actual:
        raise_assertion_error(f"{actual} is {expected}")


def assert_is_not_in(expected, actual):
    """Assert that the expected value is not in the actual value."""
    if expected in actual:
        raise_assertion_error(f"{expected} is in {actual}")


def assert_is_coroutine_function(func):
    """Assert that the function is a coroutine function."""
    if not inspect.iscoroutinefunction(func):
        raise_assertion_error(f"{func} is not a coroutine function")


def assert_is_not_coroutine_function(func):
    """Assert that the function is not a coroutine function."""
    if inspect.iscoroutinefunction(func):
        raise_assertion_error(f"{func} is a coroutine function")


def assert_is_coroutine(func):
    """Assert that the function is a coroutine."""
    if not inspect.iscoroutine(func):
        raise_assertion_error(f"{func} is not a coroutine")


def assert_is_not_coroutine(func):
    """Assert that the function is not a coroutine."""
    if inspect.iscoroutine(func):
        raise_assertion_error(f"{func} is a coroutine")


def assert_is_async_function(func):
    """Assert that the function is async."""
    if not inspect.isasyncgenfunction(func):
        raise_assertion_error(f"{func} is not async")


def assert_has_attr(obj, attr):
    """Assert that the object has the attribute."""
    if not hasattr(obj, attr):
        raise_assertion_error(f"{obj} does not have the attribute {attr}")


def assert_is_discriptor(obj):
    """Assert that the object is a descriptor."""
    if not inspect.isgetsetdescriptor(obj):
        raise_assertion_error(f"{obj} is not a descriptor")


def assert_is_not_discriptor(obj):
    """Assert that the object is not a descriptor."""
    if inspect.isgetsetdescriptor(obj):
        raise_assertion_error(f"{obj} is a descriptor")


def assert_all_not_none(iterator):
    """Assert that all values in the iterator are None."""
    filtered = filter(lambda x: x is not None, iterator)
    if any(filtered):
        raise_assertion_error(f"Not all values in {iterator} are None")


def assert_any_not_none(iterator):
    """Assert that any value in the iterator is not None."""
    filtered = filter(lambda x: x is not None, iterator)
    if not any(filtered):
        raise_assertion_error(f"No values in {iterator} are not None")


def assert_is_file_descriptor(fd):
    """Assert that the file descriptor is a file descriptor."""
    if not isinstance(fd, int):
        raise_assertion_error(f"{fd} is not a file descriptor")


def assert_is_io(fd):
    """Assert that the file descriptor is an IO object."""
    if not isinstance(fd, io.IOBase):
        raise_assertion_error(f"{fd} is not an IO object")


def assert_is_iterator(obj):
    """Assert that the object is an iterator."""
    if not hasattr(obj, "__iter__"):
        raise_assertion_error(f"{obj} is not an iterator")


def assert_is_not_iterator(obj):
    """Assert that the object is not an iterator."""
    if hasattr(obj, "__iter__"):
        raise_assertion_error(f"{obj} is an iterator")


def assert_is_iterable(obj):
    """Assert that the object is iterable."""
    try:
        iter(obj)
    except TypeError:
        raise_assertion_error(f"{obj} is not iterable")


def assert_is_generator_object(obj):
    """Assert that the object is a generator."""
    if not inspect.isgenerator(obj):
        raise_assertion_error(f"{obj} is not a generator")


def assert_is_not_generator_object(obj):
    """Assert that the object is not a generator."""
    if inspect.isgenerator(obj):
        raise_assertion_error(f"{obj} is a generator")


def assert_is_generator_function(func):
    """Assert that the function is a generator function."""
    if not inspect.isgeneratorfunction(func):
        raise_assertion_error(f"{func} is not a generator function")


def assert_is_not_generator_function(func):
    """Assert that the function is not a generator function."""
    if inspect.isgeneratorfunction(func):
        raise_assertion_error(f"{func} is a generator function")


__all__ = [
    "assert_true",
    "assert_false",
    "assert_equal",
    "assert_not_equal",
    "assert_in",
    "assert_not_in",
    "assert_is_instance",
    "assert_is_not_instance",
    "assert_is_none",
    "assert_is_not_none",
    "assert_raises",
    "assert_raises_message",
    "assert_length",
    "assert_greater_than",
    "assert_greater_than_or_equal",
    "assert_less_than",
    "assert_less_than_or_equal",
    "assert_almost_equal",
    "assert_is",
    "assert_is_subclass",
    "assert_not_is_subclass",
    "assert_is_not",
    "assert_is_not_in",
    "assert_is_coroutine_function",
    "assert_is_not_coroutine_function",
    "assert_is_coroutine",
    "assert_is_not_coroutine",
    "assert_is_async_function",
    "assert_has_attr",
    "assert_is_discriptor",
    "assert_is_not_discriptor",
    "assert_all_not_none",
    "assert_any_not_none",
    "assert_is_file_descriptor",
    "assert_is_io",
    "assert_is_iterator",
    "assert_is_not_iterator",
    "assert_is_iterable",
    "assert_is_generator_object",
    "assert_is_not_generator_object",
    "assert_is_generator_function",
    "assert_is_not_generator_function",
]
