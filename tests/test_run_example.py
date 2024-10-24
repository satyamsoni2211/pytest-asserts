from pytest import RunResult


def test_plugin(pytester):

    pytester.copy_example("test_examples.py")
    result: RunResult = pytester.runpytest()
    print(result.outlines)
